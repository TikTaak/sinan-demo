import sqlite3

class Database(object):
    db = None
    cursor = None
    def __init__(self):
        self.db = sqlite3.connect("database/db.sqlite3")
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS post(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TEXT NOT NULL
            )
        ''')
        self.db.commit()
        
