from horse import Horse
from settings import Settings
from rich.console import Console
from rich.table import Table
import database
import time

class Race:
    def __init__(self):
        self.settings = Settings()
        self.balance = database.get_balance()


    def new_race(self):
        self.horse1 = Horse.new_horse()
        self.horse2 = Horse.new_horse()
        self.horse3 = Horse.new_horse()
        self.horse4 = Horse.new_horse()

        self.race_horses = [self.horse1, self.horse2, self.horse3, self.horse4]
        self.horse_list()

        self.place_bet()


    def horse_list(self):
        console = Console()
        table = Table(title="Horse Stats")

        table.add_column("Horse", justify="left", style="cyan", no_wrap=True)
        table.add_column("Racer", justify="center", style="magenta")
        for stat in self.settings.horse_stats.keys():
            table.add_column(stat, justify="center", style="magenta")

        # Define a list of styles to cycle through for each row
        row_styles = ["dim cyan", "dim magenta", "dim green", "dim yellow"]

        for index, horse in enumerate(self.race_horses):
            stats = horse.print_horse_stats()
            table.add_row(
                horse.name,
                horse.racer,
                str(stats["speed"]),
                str(stats["stamina"]),
                str(stats["focus"]),
                str(stats["stamina"]),
                str(stats["training"]),
                style=row_styles[index % len(row_styles)]
            )

        console.print(table)

    def place_bet(self):
        print("To place a bet, first choose a horse from the list, then enter the amount you would like to bet.")
        self.bet_horse = input("Horse: ")
        while self.bet_horse not in [horse.name for horse in self]:
            print("Invalid horse name. Please choose one of the listed horses.")
            self.bet_horse = input("Horse: ")

        self.bet_amount = input("Amount: ")
        while (not self.bet_amount.isdigit()) and (self.bet_amount <= self.balance):
            print("Invalid amount. Please enter a valid number. (Balance: {})".format(self.balance))
            self.bet_amount = input("Amount: ")
        self.balance -= self.bet_amount

    def race_track(self):
        while not len(self.race_results) == 4:
            for horse in self:
                time.sleep(0.3)

                horse.update_position()
                self.check_winner()

    def check_winner(self):
        for horse in self.race_horses:
            if horse.check_horse_finish():
                self.race_results.append[horse]

    def placements(self):
        self.race_results[0] += "Takes first place"
        self.race_results[1] += "Takes second place"
        self.race_results[2] += "Takes third place"
        self.race_results[3] += "Takes fourth place"
        print(self.race_results)
    

# Example usage
if __name__ == "__main__":
    race = Race()
    race.new_race()
