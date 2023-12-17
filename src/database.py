import sqlite3

class Database(object):
    db = None
    cursor = None
    def __init__(self):
        self.db = sqlite3.connect("database/db.sqlite3")
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            post_id TEXT NOT NULL,
            post_caption TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            user_id TEXT NOT NULL
            )
        ''')
        self.db.commit()
    
    def add_post(self, post_id, post_caption, user):
        self.cursor.execute("INSERT INTO posts (post_id, post_caption, user) VALUES (?, ?, ?)",
            (post_id, post_caption, user))
        self.db.commit()
        
        
    def add_user(self, username, user_id):
        self.cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)",
            (username, user_id))
        self.db.commit()
