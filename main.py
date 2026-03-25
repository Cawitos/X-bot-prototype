from services.x_api_service import get_post_replies
from filters.text_filter import filter_valid_comments
from filters.participation_filter import first_participation_only
from logic.winner_selector import select_winners


def analizar_post(post_url, correct_answer, winners_count):
    comments = get_post_replies(post_url)

    valid_comments = filter_valid_comments(comments, correct_answer)

    unique_comments = first_participation_only(valid_comments)

    winners = select_winners(unique_comments, winners_count)

    return [w.format_output() for w in winners]


def main():
    post_url = input("URL del post: ")
    correct_answer = input("Respuesta correcta: ")
    winners_count = int(input("Cantidad de ganadores: "))

    winners = analizar_post(post_url, correct_answer, winners_count)

    print("\nGANADORES:\n")

    for w in winners:
        print(w)


if __name__ == "__main__":
    main()