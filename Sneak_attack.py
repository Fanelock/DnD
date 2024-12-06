from Weapon_main import weapon_attack
import random as rd

class Sneak_attack(weapon_attack):
    def __init__(self, str_mod, dex_mod, prof_bonus, number, dice_type):
        super().__init__(str_mod, dex_mod, prof_bonus)
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def sneak_damage(self):
        self.dmg = 0  # Reset the damage for each sneak attack calculation
        for _ in range(self.number):
            dmg_roll = rd.randint(1, self.dice_type)
            self.dmg += dmg_roll
        return self.dmg

    def __str__(self):
        return f"You Longbow deals {self.dmg} damage to the target!"