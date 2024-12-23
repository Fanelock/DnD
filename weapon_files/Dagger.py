from ..Weapon_main import WeaponAttack
from ..class_files import SneakAttack
from ..class_files import Rogue

class Dagger(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, "Dagger", "Light")
        self.number = 1
        self.dice_type = 4
        self.dmg = 0
        self.supports_sneak_attack = True

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack: SneakAttack = None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        self.dmg = self.apply_fighting_style(hit, roll, self.number, self.dice_type, dex)

        if fighting_style == None:
            if mastery:
                hit2, roll2, advantage2 = super().attack_roll(ac, dex, advantage, disadvantage)  # Second attack roll
                second_attack_dmg = self.calc_dmg(hit2, roll2, self.number, self.dice_type, dex)

                self.dmg += second_attack_dmg

                if second_attack_dmg != 0:
                    self.dmg += second_attack_dmg - self.owner.dex

        if isinstance(self.owner, Rogue):
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