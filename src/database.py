import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("horse_race.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.balance, self.previous_win, self.win_streak, self.current_win_streak = self.get_database()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS horse_race (
                balance INTEGER,
                previous_win BOOLEAN,
                win_streak INTEGER,
                current_win_streak INTEGER
            )
        ''')
        self.conn.commit()

    def update_database(self, balance, previous_win, win_streak, current_win_streak):
        self.cursor.execute('''
            INSERT INTO horse_race (balance, previous_win, win_streak, current_win_streak) 
            VALUES (?, ?, ?, ?)
        ''', (balance, previous_win, win_streak, current_win_streak))
        self.conn.commit()

    def get_database(self):
        self.cursor.execute('''
            SELECT balance, previous_win, win_streak, current_win_streak FROM horse_race ORDER BY rowid DESC LIMIT 1
        ''')
        result = self.cursor.fetchone()
        if result:
            return result[0], result[1], result[2], result[3]
        else:
            # If no data exists, initialize with default values
            return 0, False, 0, 0
