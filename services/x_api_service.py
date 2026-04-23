from services.x_client import get_replies
from models.comment_model import Comment
from utils.url_parser import extract_tweet_id


def get_post_replies(post_url):
    tweet_id = extract_tweet_id(post_url)

    response = get_replies(tweet_id)

    # DEBUG
    print("RAW RESPONSE:", response)

    if not response or "data" not in response:
        return {
            "comments": [],
            "meta": {
                "tweet_id": tweet_id,
                "total_raw": 0,
                "error": "No data returned from X API"
            }
        }

    tweets_data = response.get("data", [])
    users_data = response.get("includes", {}).get("users", [])

    users_map = {user["id"]: user["username"] for user in users_data}

    comments = []

    for item in tweets_data:
        author_id = item.get("author_id")
        username = users_map.get(author_id)

        if not username:
            continue

        comments.append(
            Comment(
                username=username,
                text=item.get("text", ""),
                created_at=item.get("created_at")
            )
        )

    return {
        "comments": comments,
        "meta": {
            "tweet_id": tweet_id,
            "total_raw": len(tweets_data),
            "total_comments": len(comments)  
        }
    }