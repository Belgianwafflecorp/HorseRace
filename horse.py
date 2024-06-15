import random
from settings import settings
from rich.console import Console
from rich.table import Table

class horse:
    def __init__(self, name, breed):
        self.name = name
        self.horse_stats = settings.horse_stats
        self.settings = settings()
        self.horse_stats = self.stats()
        self.horse_avg = self.horse_avg()
        self.position = ['H','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
        
    def new_horse(self):
        self.name = random.choice(self.settings.horse_names)
        self.settings.horse_names.pop(self.name)
        self.horse_stats = self.stats()

    def stats(self):
        for stat in self.horse_stats:
            self.horse_stats[stat] = random.randint(1, 100)
        return self.horse_stats
    
    def print_horse_stats(self):
        console = Console()
        table = Table(title=f"{self.name} Stats")

        table.add_column("Stat", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        for stat, value in self.horse_stats.items():
            table.add_row(stat, str(value))

        console.print(table)
    
    def horse_avg(self):
        return int(sum(self.horse_stats.values()) / len(self.horse_stats))
    
    def horse_run_odds(self):
        for horse in self.race_horses:
            move_odds = horse.horse_avg()
            no_move_odds = 100 - move_odds
        
            self.run_odds = {
                'move': move_odds,
                'no_move': no_move_odds
            }

            # Randomly choose between move and no_move based on the odds
            self.move_result = random.choices(['move', 'no_move'], weights=[move_odds, no_move_odds], k=1)[0]
            

    def horse_position(self):
        if self.check_horse_finish() == True:
            print(f'{self.name} has finished')
        else:
            if self.move == 'move':
                self.position.pop(-1)
                self.position.append('_')
                print(self.position)
            print(self.position)

    def horse_run(self):
        for horse in self.race_horses:
            self.move = random.choices(list(self.run_odds.keys()), k = 1, weights = self.run_odds.values)

            self.horse_position()

    def check_horse_finish(self):
        if self.position[-1] == 'H':
            return True
        else: False