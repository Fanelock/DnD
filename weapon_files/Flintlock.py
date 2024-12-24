from ..Weapon_main import WeaponAttack
from ..class_files import Rogue
from .. import AttackHandler

class Flintlock(WeaponAttack):
    def __init__(self, owner,):
        super().__init__(owner, "Flintlock", "Ranged")
        self.number = 1
        self.dice_type = 8
        self.dmg = 0
        self.supports_sneak_attack = True

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack=None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        self.dmg = self.apply_fighting_style(hit, roll, self.number, self.dice_type, dex)

        if isinstance(self.owner, Rogue):
            sneak_dmg = self.owner.perform_sneak_attack(hit, advantage)
            self.dmg += sneak_dmg


        return hit, roll, self.dmg

    def __str__(self):
        return f"You Flintlock deals {self.dmg} damage to the target!"