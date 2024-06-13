from horse import horse    
import rich
import random
from settings import settings
import os

class race:
    def __init__(self):
        self.settings = settings()
        self.horse = horse()
        
    def new_race(self):
        horse1 = horse.new_horse()
        horse2 = horse.new_horse()
        horse3 = horse.new_horse()
        horse4 = horse.new_horse()

        self.race_horses = [horse1, horse2, horse3, horse4]



    def horse_run_odds(self):
        for horse in self.race_horses:
            move_odds = horse.horse_avg()
            no_move_odds = 100 - move_odds
        
            run_odds = {
                'move': move_odds,
                'no_move': no_move_odds
            }

    def horse_position(self):
        s = '_'
        position = ['H',s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s]
        if self.move == 'move':
            position.pop(-1)
            position.append(s)
            print(position)
        print(position)

    def horse_run(self):
        for horse in self.race_horses:
            self.move = random.choices(list(self.run_odds.keys()), k = 1, weights = self.run_odds.values)

            self.horse_position()
