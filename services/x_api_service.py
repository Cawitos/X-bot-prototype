from services.x_client import get_replies
from models.comment_model import Comment
from utils.url_parser import extract_tweet_id


def get_post_replies(post_url):
    tweet_id = extract_tweet_id(post_url)

    response = get_replies(tweet_id)

    if not response or not response.data:
        return {
            "comments": [],
            "meta": {
                "tweet_id": tweet_id,
                "total_raw": 0,
                "error": "No data returned from X API"
            }
        }

    tweets_data = response.data
    users_data = response.includes.get("users", []) if response.includes else []

    users_map = {user.id: user.username for user in users_data}

    comments = []

    for item in tweets_data:
        username = users_map.get(item.author_id)

        if not username:
            continue

        comments.append(
            Comment(
                username=username,
                text=item.text,
                created_at=item.created_at
            )
        )

    return {
        "comments": comments,
        "meta": {
            "tweet_id": tweet_id,
            "total_raw": len(tweets_data),
            "total_valid": len(comments)
        }
    }