import random as rd
from Weapon_main import WeaponAttack

class Longbow(WeaponAttack):
    def __init__(self, owner, number, dice_type):
        super().__init__(owner, "Longbow")
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0
        self.supports_sneak_attack = True

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack=None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Longbow deals {self.dmg} damage to the target!"