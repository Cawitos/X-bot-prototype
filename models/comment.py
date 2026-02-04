from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comment:
    username: str
    text: str
    date: datetime
