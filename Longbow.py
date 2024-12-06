import random as rd
import matplotlib.pyplot as plt
from Weapon_main import weapon_attack

class Longbow(weapon_attack):
    def __init__(self, str_mod, dex_mod, prof_bonus):
        super().__init__(str_mod, dex_mod, prof_bonus)
        self.dmg = 0

    def calc_dmg(self, hit):
        if not hit:
            self.dmg = self.str
            return self.dmg
        else:
            dmg_roll_1 = rd.randint(1, 8)
            self.dmg = dmg_roll_1 + self.str
        return self.dmg

    def __str__(self):
        return f"You Longbow deals {self.dmg} damage to the target!"