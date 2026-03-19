from datetime import datetime


class Comment:

    def __init__(self, username, text, created_at):
        self.username = username
        self.text = text

        # Convertir string ISO a datetime
        self.created_at = datetime.fromisoformat(
            created_at.replace("Z", "+00:00")
        )

    def format_output(self):
        return f"@{self.username} | {self.text} // {self.created_at}"