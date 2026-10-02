from datetime import datetime


class Comment:

    def __init__(self, username, text, created_at, tweet_id=None):
        self.username = username
        self.text = text
        self.tweet_id = tweet_id

        # Convertir string ISO a datetime
        self.created_at = datetime.fromisoformat(
            created_at.replace("Z", "+00:00")
        )

    @property
    def url(self):
        if self.tweet_id:
            return f"https://x.com/{self.username}/status/{self.tweet_id}"
        return None

    def format_output(self):
        return f"@{self.username} | {self.text} // {self.created_at} // {self.url}"