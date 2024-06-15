from horse import Horse
from settings import Settings
from rich.console import Console
from rich.table import Table

class Race:
    def __init__(self):
        self.settings = Settings()

    def new_race(self):
        self.horse1 = Horse.new_horse()
        self.horse2 = Horse.new_horse()
        self.horse3 = Horse.new_horse()
        self.horse4 = Horse.new_horse()

        self.race_horses = [self.horse1, self.horse2, self.horse3, self.horse4]

        self.horse_list()

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

# Example usage
if __name__ == "__main__":
    race = Race()
    race.new_race()
