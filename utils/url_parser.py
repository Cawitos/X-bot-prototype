import re


def extract_tweet_id(post_url: str) -> str:

    pattern = r"status/(\d+)"
    match = re.search(pattern, post_url)

    if not match:
        raise ValueError("No se pudo extraer el tweet_id de la URL.")

    return match.group(1)