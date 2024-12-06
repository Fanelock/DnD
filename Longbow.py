import random as rd
from Weapon_main import weapon_attack

class Longbow(weapon_attack):
    def __init__(self, str_mod, dex_mod, prof_bonus, number, dice_type):
        super().__init__(str_mod, dex_mod, prof_bonus)
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0

    def perform_attack(self, ac, dex, mastery, fighting_style):
        hit, roll = super().attack_roll(ac, dex)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Longbow deals {self.dmg} damage to the target!"