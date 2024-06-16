import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("horse_race.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.balance = self.get_balance()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS horse_race (
                balance INTEGER
            )
        ''')
        self.conn.commit()

    def update_balance(self, balance):
        self.cursor.execute('''
            INSERT INTO horse_race (balance) VALUES (?)
        ''', (balance,))
        self.conn.commit()

    def get_balance(self):
        self.cursor.execute('''
            SELECT balance FROM horse_race ORDER BY ROWID DESC LIMIT 1
        ''')
        result = self.cursor.fetchone()
        return result[0] if result else 0
