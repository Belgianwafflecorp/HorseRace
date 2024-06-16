from horse import Horse
from settings import Settings
from rich.console import Console
from rich.table import Table
import rich
import database
import time

class Race:
    def __init__(self):
        self.settings = Settings()
        self.db = database.Database()
        self.balance = self.db.get_balance()
        self.race_results = []  # Initialize race results as an empty list for each race instance

    def new_race(self):
        self.check_broke()
        self.horse1 = Horse.new_horse()
        self.horse2 = Horse.new_horse()
        self.horse3 = Horse.new_horse()
        self.horse4 = Horse.new_horse()

        self.race_horses = [self.horse1, self.horse2, self.horse3, self.horse4]
        self.horse_list()

        self.place_bet()
        self.race_track()
        self.placements()
        self.player_winnings()

    def deposit(self):
        deposit_amount = input("Enter the amount you would like to deposit: ")
        while not deposit_amount.isdigit():
            print("Invalid amount. Please enter a valid number.")
            deposit_amount = input("Enter the amount you would like to deposit: ")
        deposit_amount = int(deposit_amount)
        self.balance += deposit_amount
        self.db.update_balance(self.balance)
        print(f"Successfully deposited {deposit_amount}. Your new balance is {self.balance}.")

    def check_broke(self):
        if self.balance == 0:
            print("You have no money left. Please deposit more to continue.")
            self.deposit()

    def horse_list(self):
        self.console = Console()
        self.table = Table(title="Horse Stats")

        self.table.add_column("Horse", justify="left", style="cyan", no_wrap=True)
        self.table.add_column("Racer", justify="center", style="magenta")
        for stat in self.settings.horse_stats.keys():
            self.table.add_column(stat, justify="center", style="magenta")

        # Define a list of styles to cycle through for each row
        row_styles = ["dim cyan", "dim magenta", "dim green", "dim yellow"]

        for index, horse in enumerate(self.race_horses):
            stats = horse.horse_stats
            self.table.add_row(
                horse.name,
                horse.racer,
                str(stats["speed"]),
                str(stats["strength"]),
                str(stats["focus"]),
                str(stats["stamina"]),
                str(stats["training"]),
                style=row_styles[index % len(row_styles)]
            )

        self.console.print(self.table)

    def place_bet(self):
        print("To place a bet, first choose a horse or racer from the list, then enter the amount you would like to bet.")
        self.bet_horse = input("Horse/Racer: ").strip().lower()  # Convert input to lowercase
        horse_names = [horse.name.lower() for horse in self.race_horses]  # Convert horse names to lowercase
        racer_names = [horse.racer.lower() for horse in self.race_horses]  # Convert racer names to lowercase

        while self.bet_horse not in horse_names and self.bet_horse not in racer_names:
            self.clear_screen()
            self.console.print(self.table)
            print("Invalid horse or racer name. Please choose one of the listed horses or racers.")
            self.bet_horse = input("Horse/Racer: ").strip().lower()  # Ask again and convert input to lowercase

        self.bet_amount = input("Amount: ")
        while not self.bet_amount.isdigit() or int(self.bet_amount) > self.balance:
            self.clear_screen()
            self.console.print(self.table)
            print("Invalid amount. Please enter a valid number. (Balance: {})".format(self.balance))
            print(f"How much would you like to bet on {self.bet_horse}.")
            self.bet_amount = input("Amount: ")

        self.bet_amount = int(self.bet_amount)
        self.balance -= self.bet_amount
        self.db.update_balance(self.balance)
        self.clear_screen()


    def race_track(self):
        while len(self.race_results) < len(self.race_horses):
            for horse in self.race_horses:
                horse.update_position()
                print(horse.name)
                print(''.join(map(str, horse.position)))
                if horse.check_horse_finish() and horse not in self.race_results:
                    self.race_results.append(horse)
            time.sleep(0.3)
            self.clear_screen()

    def placements(self):
        self.placementsList = ["first", "second", "third", "fourth"]
        for i, horse in enumerate(self.race_results):
            print(f"{horse.name} takes {self.placementsList[i]} place.")

    def player_winnings(self):
        if not self.race_results:
            print("No race results available. Race might not have been completed properly.")
            return
        
        if self.bet_horse == self.race_results[0].name.lower():
            winnings = self.bet_amount * 2
            self.balance += winnings
            self.db.update_balance(self.balance)
            print(f"\nCongratulations! You won {winnings}!\n")
            print(f"Your balance is: {self.balance}.\n")
        else:
            print("\nBetter luck next time!\n")
            print(f"Your balance is: {self.balance}.\n")
        input("Press Enter to continue...")
        self.clear_screen()

    def clear_screen(self):
        print("\033c")

# Example usage
if __name__ == "__main__":
    while True:
        race = Race() 
        race.new_race()
