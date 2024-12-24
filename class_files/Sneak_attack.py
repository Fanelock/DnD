from DND_weapons.Weapon_main import WeaponAttack
import random as rd
import math

class SneakAttack(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, "Sneak Attack", None)
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def sneak_damage(self, hit, roll):
        dice_number = math.ceil(self.owner.level/2)
        dmg = 0  # Reset the damage for each sneak attack calculation
        if hit:  # Only calculate sneak attack if the attack hits
            if roll == 20:  # Critical hit doubles the dice
                for _ in range(2 * dice_number):
                    dmg_roll = rd.randint(1, 6)
                    dmg += dmg_roll
            else:  # Normal hit
                for _ in range(dice_number):
                    dmg_roll = rd.randint(1, 6)
                    dmg += dmg_roll
        return dmg

    def __str__(self):
        pass