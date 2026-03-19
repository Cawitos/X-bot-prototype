from services.x_client import get_replies
from models.comment_model import Comment
from utils.url_parser import extract_tweet_id


def get_post_replies(post_url):

    tweet_id = extract_tweet_id(post_url)

    response = get_replies(tweet_id)

    if "data" not in response:
        print("No se encontraron replies para este tweet.")
        return []

    tweets_data = response.get("data", [])
    users_data = response.get("includes", {}).get("users", [])

    # Mapa author_id → username
    users_map = {user["id"]: user["username"] for user in users_data}

    comments = []

    for item in tweets_data:

        author_id = item["author_id"]
        username = users_map.get(author_id)

        if not username:
            continue  # evitar usuarios desconocidos

        comments.append(
            Comment(
                username=username,
                text=item["text"],
                created_at=item["created_at"]
            )
        )

    return comments