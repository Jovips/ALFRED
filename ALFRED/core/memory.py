import sqlite3
from datetime import datetime

class Memory:
    def __init__(self, db_path="alfred_memory.db", limit=20):
        self.limit = limit
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def add(self, role, content):
        self.cursor.execute(
            "INSERT INTO messages (role, content, timestamp) VALUES (?, ?, ?)",
            (role, content, datetime.now().isoformat())
        )
        self.conn.commit()

    def get_context(self):
        self.cursor.execute(
            "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?",
            (self.limit,)
        )
        rows = self.cursor.fetchall()

        
        rows.reverse()

        return [{"role": r, "content": c} for r, c in rows]
