import random
from settings import Settings

class Horse:
    used_horse_names = set()
    used_racer_names = set()

    def __init__(self, name, racer):
        self.name = name
        self.racer = racer
        self.settings = Settings()
        self.horse_stats = self.stats()
        self.horse_avg = self.calculate_avg()
        self.horse_icon = '🏇'
        self.track = '_'
        self.position = ([self.track] * 23) + [self.horse_icon]

    @classmethod
    def reset_names(cls):
        cls.available_horse_names = list(cls.used_horse_names)
        cls.available_racer_names = list(cls.used_racer_names)
        cls.used_horse_names.clear()
        cls.used_racer_names.clear()

    @classmethod
    def new_horse(cls):
        settings = Settings()

        # Select unique horse name
        available_horse_names = list(set(settings.horse_names) - cls.used_horse_names)
        if not available_horse_names:
            raise ValueError("No more unique horse names available")
        name = random.choice(available_horse_names)
        cls.used_horse_names.add(name)
        
        # Select unique racer name
        available_racer_names = list(set(settings.racer_names) - cls.used_racer_names)
        if not available_racer_names:
            raise ValueError("No more unique racer names available")
        racer = random.choice(available_racer_names)
        cls.used_racer_names.add(racer)

        settings.horse_names.remove(name)
        settings.racer_names.remove(racer)

        return Horse(name, racer)

    def stats(self):
        horse_stats = {stat: random.randint(10, 100) for stat in self.settings.horse_stats}
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
        if self.check_horse_finish():
            self.position = ["🏁"] + ([self.track] * 23)  # Mark as finished with a flag
        elif move == 'move' and '_' in self.position:
            self.position.pop(0)  # Remove the first character (move forward)
            self.position.append('_')  # Append a new track character at the end


    def check_horse_finish(self):
        return self.position[0] == (self.horse_icon or '🏁')
