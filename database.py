import sqlite3

def __init__(self):
    self.conn = sqlite3.connect
    self.cursor = self.conn.cursor()
    self.balance = self.get_balance()

def create_table(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS horse_race (
            balance INTEGER,
        )
    ''')
    self.conn.commit()

def update_balance(self, balance):
    self.cursor.execute('''
        INSERT INTO horses (balance) VALUES (?)
    ''', (self.balance,))
    self.conn.commit()

def get_balance(self):
    self.cursor.execute('''
        SELECT balance FROM horse_race
    ''')
    return self.cursor.fetchone()[0]