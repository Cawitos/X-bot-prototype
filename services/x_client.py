import requests
import os


def get_replies(tweet_id):

    bearer_token = os.getenv("X_BEARER_TOKEN")

    if not bearer_token:
        raise Exception("No se encontró la variable de entorno X_BEARER_TOKEN")

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    url = "https://api.x.com/2/tweets/search/recent"

    params = {
        "query": f"conversation_id:{tweet_id}",
        "tweet.fields": "author_id,created_at,text",
        "expansions": "author_id",
        "user.fields": "username",
        "max_results": 100
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(
            f"Error API X: {response.status_code} - {response.text}"
        )

    return response.json()