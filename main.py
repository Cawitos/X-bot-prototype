from scraper.x_scraper import get_replies
from analyzer.exact_matcher import find_exact_matches


def main():

    post_url = input("url del post de X ")
    target_text = input("texto exacto a buscar ")

    comments = get_replies(post_url)

    matches = find_exact_matches(comments, target_text)

    matches.sort(key=lambda x: x.date)

    print("\nResultados:\n")

    for match in matches:
        print(f"{match.username} | {match.text} // {match.date}")


if __name__ == "__main__":
    main()
