from Weapon_main import WeaponAttack
from Sneak_attack import SneakAttack
from Rogue_class import Rogue

class Shortsword(WeaponAttack):
    def __init__(self, owner, number, dice_type):
        super().__init__(owner, "Shortsword")
        self.number = number
        self.dice_type = dice_type
        self.dmg = 0
        self.supports_sneak_attack = True

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack: SneakAttack = None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        if isinstance(self.owner, Rogue):
            sneak_dmg = self.owner.perform_sneak_attack(hit, advantage)
            self.dmg += sneak_dmg

        return hit, roll, self.dmg

    def __str__(self):
        return f"You Shortsword deals {self.dmg} damage to the target!"