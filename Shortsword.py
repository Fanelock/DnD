from Weapon_main import weapon_attack
from Sneak_attack import Sneak_attack

class Shortsword(weapon_attack):
    def __init__(self, str_mod, dex_mod, prof_bonus, number, dice_type):
        super().__init__(str_mod, dex_mod, prof_bonus)
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack: Sneak_attack = None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        if advantage and hit:
            sneak_dmg = sneak_attack.sneak_damage()  # Create an instance and call sneak_damage method
            self.dmg += sneak_dmg

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Shortsword deals {self.dmg} damage to the target!"