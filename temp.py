import requests
import os

# 🔹 Pega aquí el tweet de prueba
tweet_id = "2019427568085295294"  # ← el que usaste antes

bearer_token = os.getenv("X_BEARER_TOKEN")

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

url = "https://api.x.com/2/tweets/search/recent"

params = {
    "query": f"conversation_id:{tweet_id}",
    "tweet.fields": "author_id,created_at,text",
    "expansions": "author_id",
    "user.fields": "username",
    "max_results": 10
}

response = requests.get(url, headers=headers, params=params)

print("STATUS:", response.status_code)
data = response.json()

print("\nRAW RESPONSE:\n", data)


# 🔥 Parseo limpio (lo que usará tu bot)
tweets = data.get("data", [])
users = data.get("includes", {}).get("users", [])

# Mapa id → username
users_map = {user["id"]: user["username"] for user in users}

print("\nRESPONSES PROCESADAS:\n")

for tweet in tweets:
    username = users_map.get(tweet["author_id"], "unknown")
    text = tweet["text"]
    created_at = tweet["created_at"]

    print(f"@{username} | {text} // {created_at}")