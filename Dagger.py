from Weapon_main import weapon_attack
from Sneak_attack import Sneak_attack

class Dagger(weapon_attack):
    def __init__(self, str_mod, dex_mod, prof_bonus, number, dice_type):
        super().__init__(str_mod, dex_mod, prof_bonus)
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack: Sneak_attack = None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        if mastery:
            hit2, roll2, advantage2 = super().attack_roll(ac, dex, advantage, disadvantage)  # Second attack roll
            second_attack_dmg = self.calc_dmg(hit2, roll2, self.number, self.dice_type, dex)

            self.dmg += second_attack_dmg

            if second_attack_dmg != 0:
                self.dmg += second_attack_dmg - self.dex

        sneak_attack_applied = False  # Flag to track if sneak attack has been applied

        # Apply sneak attack only once, regardless of whether the first or second attack hits
        if (advantage and hit and not sneak_attack_applied):
            sneak_dmg = sneak_attack.sneak_damage()
            self.dmg += sneak_dmg
            sneak_attack_applied = True  # Set the flag to True so that we don't apply it again

        if (advantage and hit2 and not sneak_attack_applied):  # Only apply sneak attack if it's not already applied
            sneak_dmg = sneak_attack.sneak_damage()
            self.dmg += sneak_dmg
            sneak_attack_applied = True

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Dagger deals {self.dmg} damage to the target!"