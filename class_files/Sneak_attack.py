from DND_weapons.Weapon_main import WeaponAttack
import random as rd
import math

class SneakAttack(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, name="Sneak Attack")
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def sneak_damage(self):
        dice_number = math.ceil(self.owner.level/2)
        dmg = 0  # Reset the damage for each sneak attack calculation
        for _ in range(dice_number):
            dmg_roll = rd.randint(1, 6)
            dmg += dmg_roll
        return dmg

    def __str__(self):
        pass