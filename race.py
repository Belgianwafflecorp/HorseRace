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



    
