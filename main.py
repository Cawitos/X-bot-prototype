import re
from services.x_api_service import get_post_replies
from filters.text_filter import filter_valid_comments
from filters.participation_filter import first_participation_only
from logic.winner_selector import select_winners


#Regex globales
STAKE_REGEX = re.compile(r"Stake:\s*(\w+)", re.IGNORECASE)
BET_REGEX = re.compile(r"(sport:\d+|casino:\d+)", re.IGNORECASE)


def analizar_post(
    post_url,
    correct_answer=None,
    winners_count=None,
    extract_usernames=False,
    extract_bet_ids=False,
    bet_type="all"
):
    # Obtener datos desde API
    response = get_post_replies(post_url)

    comments = response.get("comments", [])
    meta = response.get("meta", {})

    print("TWEET ID:", meta.get("tweet_id"))
    print("TOTAL RAW:", meta.get("total_raw"))
    print("TOTAL COMMENTS:", len(comments))

    # Inicializar contenedores
    usernames = []
    bet_ids = []

    # Extracción sobre TODOS los comentarios
    for c in comments:
        text = getattr(c, "text", "")

        # usernames
        if extract_usernames:
            matches = STAKE_REGEX.findall(text)
            usernames.extend(matches)

        # bet ids
        if extract_bet_ids:
            matches = BET_REGEX.findall(text)

            if bet_type == "sport":
                matches = [m for m in matches if m.lower().startswith("sport")]
            elif bet_type == "casino":
                matches = [m for m in matches if m.lower().startswith("casino")]

            bet_ids.extend(matches)

    response_data = {}

    # LÓGICA ACTUAL DE GANADORES (solo si aplica)
    if correct_answer and winners_count:
        valid_comments = filter_valid_comments(comments, correct_answer)
        print("VALID COMMENTS:", len(valid_comments))

        unique_comments = first_participation_only(valid_comments)
        print("UNIQUE COMMENTS:", len(unique_comments))

        winners = select_winners(unique_comments, winners_count)
        print("WINNERS:", len(winners))

        if not winners:
            response_data["ganadores"] = ["No hubo ganadores"]
        else:
            response_data["ganadores"] = [w.format_output() for w in winners]

    # Features
    if extract_usernames:
        response_data["usernames"] = list(set(usernames))

    if extract_bet_ids:
        response_data["bet_ids"] = list(set(bet_ids))

    # Stats
    response_data["stats"] = {
        "tweet_id": meta.get("tweet_id"),
        "total_raw": meta.get("total_raw"),
        "total_comments": len(comments),
        "unique_usernames": len(set(usernames)),
        "unique_bet_ids": len(set(bet_ids))
    }

    return response_data


# Modo consola(testing)
def main():
    post_url = input("URL del post: ")
    correct_answer = input("Respuesta correcta: ")
    winners_count = int(input("Cantidad de ganadores: "))

    result = analizar_post(
        post_url,
        correct_answer,
        winners_count,
        extract_usernames=True,
        extract_bet_ids=True
    )

    print("\nRESULTADO:\n")

    if "ganadores" in result:
        print("GANADORES:\n")
        for w in result["ganadores"]:
            print(w)

    if "usernames" in result:
        print("\nUSERNAMES:\n")
        for u in result["usernames"]:
            print(u)

    if "bet_ids" in result:
        print("\nBET IDS:\n")
        for b in result["bet_ids"]:
            print(b)

    print("\nSTATS:\n", result["stats"])


if __name__ == "__main__":
    main()