import json
from models.comment_model import Comment


def get_post_replies(post_url):

    with open("mock_data/sample_replies.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    comments = []

    for item in data:
        comments.append(
            Comment(
                item["username"],
                item["text"],
                item["created_at"]
            )
        )

    return comments