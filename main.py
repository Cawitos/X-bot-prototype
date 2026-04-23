import re
from services.x_api_service import get_post_replies
from filters.participation_filter import first_participation_only
from logic.winner_selector import select_winners


# =========================
# REGEX
# =========================

STAKE_REGEX = re.compile(
    r"(?:stake\s*id|user\s*id|id|user)[:\-]?\s*(\w+)",
    re.IGNORECASE
)

BET_REGEX = re.compile(r"(sport:\d+|casino:\d+)", re.IGNORECASE)
X_USER_REGEX = re.compile(r"@\w+")


# =========================
# HELPERS
# =========================

def normalizar_texto(texto):
    return texto.lower().strip()


def parse_respuestas(respuesta):
    return [normalizar_texto(r) for r in respuesta.split(",")]


def comentario_valido_multiple(texto, respuestas_correctas):
    texto = normalizar_texto(texto)

    palabras = re.split(r"[,\n]+", texto)
    palabras = [p.strip() for p in palabras if p.strip()]

    return set(respuestas_correctas).issubset(set(palabras))


# =========================
# MAIN LOGIC
# =========================

def analizar_post(
    url,
    respuesta=None,
    ganadores=None,
    extract_usernames=False,
    extract_bet_ids=False,
    bet_type="all"
):
    # =========================
    # OBTENER DATA
    # =========================
    response = get_post_replies(url)

    comments = response.get("comments", [])
    meta = response.get("meta", {})

    print("TWEET ID:", meta.get("tweet_id"))
    print("TOTAL RAW:", meta.get("total_raw"))
    print("TOTAL COMMENTS:", len(comments))

    usernames = []
    bet_ids = []
    winners = []
    response_data = {}

    # =========================
    # EXTRACCIÓN GENERAL
    # =========================
    for c in comments:
        text = getattr(c, "text", "")

        # USERNAMES
        if extract_usernames:
            stake_matches = STAKE_REGEX.findall(text)
            usernames.extend(stake_matches)
            usernames.append(f"@{c.username}")

        # BET IDS
        if extract_bet_ids:
            matches = BET_REGEX.findall(text)

            if bet_type == "sport":
                matches = [m for m in matches if m.lower().startswith("sport")]
            elif bet_type == "casino":
                matches = [m for m in matches if m.lower().startswith("casino")]

            bet_ids.extend(matches)

    # =========================
    # LÓGICA DE GANADORES
    # =========================

    respuestas_correctas = parse_respuestas(respuesta) if respuesta else None
    valid_comments = []

    # CASO 1: HAY RESPUESTA
    if respuesta:

        for c in comments:
            text = getattr(c, "text", "")

            # RESPUESTA MULTIPLE
            if "," in respuesta:
                if comentario_valido_multiple(text, respuestas_correctas):
                    valid_comments.append(c)

            # RESPUESTA SIMPLE
            else:
                if normalizar_texto(respuesta) in normalizar_texto(text):
                    valid_comments.append(c)

        print("VALID COMMENTS:", len(valid_comments))

        unique_comments = first_participation_only(valid_comments)
        print("UNIQUE COMMENTS:", len(unique_comments))

        if ganadores:
            winners = select_winners(unique_comments, ganadores)
        else:
            winners = unique_comments

    # CASO 2: NO HAY RESPUESTA → RANDOM PURO
    else:
        print("MODO RANDOM SIN RESPUESTA")

        unique_comments = first_participation_only(comments)
        print("UNIQUE COMMENTS:", len(unique_comments))

        if ganadores:
            winners = select_winners(unique_comments, ganadores)
        else:
            winners = unique_comments

    # =========================
    # FORMATEO GANADORES (OBJETO)
    # =========================
    formatted_winners = []

    for w in winners:
        text = getattr(w, "text", "")

        x_user = f"@{getattr(w, 'username', 'unknown')}"

        stake_match = STAKE_REGEX.search(text)
        stake_user = stake_match.group(1) if stake_match else "N/A"

        formatted_winners.append({
            "x_user": x_user,
            "stake_id": stake_user,
            "comment": text
        })

    if formatted_winners:
        response_data["ganadores"] = formatted_winners
    else:
        response_data["ganadores"] = []

    # =========================
    # FEATURES EXTRA
    # =========================
    if extract_usernames:
        response_data["usernames"] = list(set(usernames))

    if extract_bet_ids:
        response_data["bet_ids"] = list(set(bet_ids))

    # =========================
    # STATS
    # =========================
    response_data["stats"] = {
        "tweet_id": meta.get("tweet_id"),
        "total_raw": meta.get("total_raw"),
        "total_comments": len(comments),
        "unique_usernames": len(set(usernames)),
        "unique_bet_ids": len(set(bet_ids))
    }

    return response_data


# =========================
# MODO CONSOLA (TEST)
# =========================
def main():
    post_url = input("URL del post: ")
    respuesta = input("Respuesta correcta (opcional, separada por comas): ")
    ganadores_input = input("Cantidad de ganadores (opcional): ")

    ganadores = int(ganadores_input) if ganadores_input else None

    result = analizar_post(
        post_url,
        respuesta if respuesta else None,
        ganadores,
        extract_usernames=True,
        extract_bet_ids=True
    )

    print("\nRESULTADO:\n")

    if "ganadores" in result:
        print("GANADORES:\n")
        for w in result["ganadores"]:
            print(f"{w['x_user']} | Stake: {w['stake_id']} | {w['comment']}")

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