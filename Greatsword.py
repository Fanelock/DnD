import random as rd
from Weapon_main import WeaponAttack

class Greatsword(WeaponAttack):
    def __init__(self, owner, number, dice_type):
        super().__init__(owner, "Greatsword")
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0
        self.supports_sneak_attack = False

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack=None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        if mastery == True and hit:
            adjusted_dmg = 0
            for _ in range(self.number):
                dmg_roll = max(rd.randint(1, self.dice_type), 3)
                adjusted_dmg += dmg_roll
            adjusted_dmg += self.owner.str
            self.dmg = adjusted_dmg

        elif mastery == True and roll == 20:
            adjusted_dmg = 0
            for _ in range(2*self.number):
                dmg_roll = max(rd.randint(1, self.dice_type), 3)
                adjusted_dmg += dmg_roll
            adjusted_dmg +=  self.owner.str
            self.dmg = adjusted_dmg

        if self.dmg == 0 and fighting_style == True:
            self.dmg = self.owner.str

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Greatsword deals {self.dmg} damage to the target!"

