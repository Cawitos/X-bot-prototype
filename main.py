from scraper.x_scraper import get_replies
import config


def main():

    replies = get_replies(
        config.POST_URL,
        config.TARGET_TEXTS,
        config.MAX_SCROLL
    )

    print("\nRESULTADOS:\n")

    if not replies:
        print("No hubo coincidencias")

    for r in replies:
        print(r)


if __name__ == "__main__":
    main()