from datetime import datetime


class Comment:

    def _init_(self, username, text, created_at):
        self.username = username
        self.text = text
        self.created_at = datetime.fromisoformat(
            created_at.replace("Z", "+00:00")
        )

    def format_output(self):
        return f"@{self.username} | {self.text} // {self.created_at}"