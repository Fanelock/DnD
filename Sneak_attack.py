from Weapon_main import WeaponAttack
import random as rd

class SneakAttack(WeaponAttack):
    def __init__(self, owner, number, dice_type):
        super().__init__(owner, name="Sneak Attack")
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def sneak_damage(self):
        dmg = 0  # Reset the damage for each sneak attack calculation
        for _ in range(self.number):
            dmg_roll = rd.randint(1, self.dice_type)
            dmg += dmg_roll
        return dmg

    def __str__(self):
        return f"Sneak attack: {self.number}d{self.dice_type} damage."