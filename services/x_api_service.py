from services.x_client import get_replies
from models.comment_model import Comment
from utils.url_parser import extract_tweet_id
from collections import Counter


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

    print("=" * 60)
    print("META:", response.get("meta"))
    print("TWEETS RECIBIDOS:", len(tweets_data))
    print("USUARIOS EN INCLUDES:", len(users_data))
    print("=" * 60)

    counter = Counter()

    users_map = {user["id"]: user["username"] for user in users_data}

    comments = []

    for item in tweets_data:
        author_id = item.get("author_id")
        username = users_map.get(author_id)

        if username:
            counter[username] += 1

        print(
            author_id,
            "->",
            username,
            "|",
            item.get("text", "")[:40]
        )

        if not username:
            continue

        comments.append(
            Comment(
                username=username,
                text=item.get("text", ""),
                created_at=item.get("created_at")
            )
        )

    # ===== ESTADÍSTICAS =====
    print("\n===== TOP 10 USUARIOS =====")

    for username, cantidad in counter.most_common(10):
        print(f"{username}: {cantidad}")

    print("\nTOTAL USUARIOS ÚNICOS:", len(counter))
    print("TOTAL COMMENTS:", len(comments))
    print("=" * 60)

    return {
        "comments": comments,
        "meta": {
            "tweet_id": tweet_id,
            "total_raw": len(tweets_data),
            "total_comments": len(comments)
        }
    }