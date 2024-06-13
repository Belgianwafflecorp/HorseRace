import random
from settings import settings

class horse:
    def __init__(self, name, breed):
        self.name = name
        self.horse_stats = settings.horse_stats
        self.settings = settings()
        
    def new_horse(self):
        self.name = random.choice(self.settings.horse_names)
        self.settings.horse_names.pop(self.name)
        self.horse_stats = self.stats()

    def stats(self):
        for stat in self.horse_stats:
            self.horse_stats[stat] = random.randint(1, 100)
        return self.horse_stats
    
    def horse_avg(self):
        return sum(self.horse_stats.values()) / len(self.horse_stats)
    
    