import random
from settings import Settings

class Horse:
    def __init__(self, name, racer):
        self.name = name
        self.racer = racer
        self.settings = Settings()
        self.horse_stats = self.stats()
        self.horse_avg = self.calculate_avg()
        self.horse_icon = '🐎'
        self.position = [self.horse_icon] + ['_'] * 20

    @staticmethod
    def new_horse():
        settings = Settings()
        name = random.choice(settings.horse_names)
        racer = random.choice(settings.racer_names)
        settings.horse_names.remove(name)
        settings.racer_names.remove(racer)
        return Horse(name, racer)

    def stats(self):
        horse_stats = {stat: random.randint(1, 100) for stat in self.settings.horse_stats}
        return horse_stats

    def print_horse_stats(self):
        return self.horse_stats

    def calculate_avg(self):
        return int(sum(self.horse_stats.values()) / len(self.horse_stats))

    def horse_run_odds(self):
        move_odds = self.calculate_avg()
        no_move_odds = 100 - move_odds

        run_odds = {
            'move': move_odds,
            'no_move': no_move_odds
        }

        move_result = random.choices(['move', 'no_move'], weights=[move_odds, no_move_odds], k=1)[0]
        return move_result

    def update_position(self):
        move = self.horse_run_odds()
        if move == 'move' and '_' in self.position:
            self.position.pop()  # Remove the last character
            self.position.insert(0, '_')  # Insert a new character at the start

        if self.check_horse_finish():
            print(f'{self.name} has finished')

    def check_horse_finish(self):
        return self.position[-1] == self.horse_icon
