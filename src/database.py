import sqlite3
import os


class Database:

    def __init__(
        self,
    ):
        self.open()

    def open(self):
        self.conn = sqlite3.connect("horse_race")
        self.cursor = self.conn.cursor()
        self.__create_table()

    # with default values
    def __create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS horse_race(balance INTEGER, previous_win BOOLEAN, win_streak INTEGER, current_win_streak INTEGER)"
        )
        self.conn.commit()

    def insert_data(
        self,
        balence,
        previous_win,
        win_streak,
        current_win_streak,
    ):
        self.cursor.execute(
            "INSERT INTO data VALUES(?, ?, ?, ?)",
            (
                balence,
                previous_win,
                win_streak,
                current_win_streak,
            ),
        )
        self.conn.commit()

    # show all data
    def get_data(self):
        self.cursor.execute("SELECT * FROM horse_race")
        return self.cursor.fetchall()

    # print the column data
    def get_column(self, column):  # show specific column
        self.cursor.execute(f"SELECT {column} FROM horse_race")
        return self.cursor.fetchone()[0]

    def add_column(self, column, data):  # add a new column
        self.cursor.execute(f"ALTER TABLE data ADD COLUMN {column} {data}")
        self.conn.commit()

    # update all data at once
    def update_data(
        self,
        balance,
        previous_win,
        win_streak,
        current_win_streak,
    ):
        if not self.get_data():
            self.insert_data(
                balance,
                previous_win,
                win_streak,
                current_win_streak,
            )
            return
        self.cursor.execute(
            "UPDATE horse_race SET balance = ?, previous_win = ?, win_streak = ?, current_win_streak = ?"
            (
                balance,
                previous_win,
                win_streak,
                current_win_streak,
            ),
        )
        self.conn.commit()

    def insert_column(self, column, value):
        self.cursor.execute(f"INSERT INTO horse_race({column}) VALUES(?)", (value,))
        self.conn.commit()

    def get_column_names(self):
        self.cursor.execute("PRAGMA table_info(horse_race)")
        return self.cursor.fetchall()

    # update a specific column or create a new one if not exist
    def update_column(self, column, value):
        if column not in [i[1] for i in self.get_column_names()]:
            # alter
            self.cursor.execute(f"ALTER TABLE horse_race ADD COLUMN {column} INTEGER")
            self.conn.commit()
        if not self.get_data():
            self.insert_column(column, value)
            return

        self.cursor.execute(f"UPDATE horse_race SET {column} = ?", (value,))
        self.conn.commit()

    # increment a specific column
    def increment_column(self, column):
        if not self.get_data():
            self.insert_column(column, 1)
            return
        self.cursor.execute(f"UPDATE horse_race SET {column} = {column} + 1")
        self.conn.commit()

    # decrement a specific column
    def decrement_column(self, column):
        if not self.get_data():
            self.insert_column(column, 0)
            return
        self.cursor.execute(f"UPDATE horse_race SET {column} = {column} - 1")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()

    # delete all data
    def delete_all_player_data(self):
        self.cursor.execute("DELETE FROM horse_race")
        self.conn.commit()