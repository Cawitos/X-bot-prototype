class Comment:

    def __init__(self, username, text, created_at):
        self.username = username
        self.text = text
        self.created_at = created_at

    def format_output(self):
        return f"@{self.username} | {self.text} // {self.created_at}"