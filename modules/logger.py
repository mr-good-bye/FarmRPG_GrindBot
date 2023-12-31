import sqlite3
from datetime import datetime


creation_script = """
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seconds UNSIGNED BIGINT,
    level TEXT,
    message TEXT,
    sender TEXT
)
"""


class Logger:
    def __init__(self, name: str):
        self.name = name
        self.db = sqlite3.connect(f'logs/{name}.db')
        self.cursor = self.db.cursor()
        self.cursor.execute(creation_script)

    def log(self, level: str, message: str, sender: str):
        self.cursor.execute(
            'INSERT INTO logs (seconds, level, message, sender) VALUES (?, ?, ?, ?)',
            (int(datetime.now().timestamp()*100), level, message, sender)
        )
        self.db.commit()


datetime.now().timestamp()
