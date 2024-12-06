
import random as rd
from abc import ABC, abstractmethod

class weapon_attack(ABC):
    def __init__(self, str_mod, dex_mod, prof_bonus):
        self.str = str_mod
        self.dex = dex_mod
        self.prof = prof_bonus
        self.hit_roll = 0

    def attack_roll(self, ac, dex):
        self.hit_roll = rd.randint(1,20)
        if dex:
            total = self.hit_roll + self.dex + self.prof
        else:
            total = self.hit_roll + self.str + self.prof
        return total >= ac

    @abstractmethod
    def calc_dmg(self):
        pass












