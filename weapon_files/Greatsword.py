import random as rd

from .. import AttackHandler
from ..Weapon_main import WeaponAttack

class Greatsword(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, "Greatsword")
        self.number = 2
        self.dice_type = 6
        self.dmg = 0
        self.supports_sneak_attack = False

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack=None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        if self.owner.level >= 2:
            if fighting_style == True and hit:
                adjusted_dmg = 0
                for _ in range(self.number):
                    dmg_roll = max(rd.randint(1, self.dice_type), 3)
                    adjusted_dmg += dmg_roll
                adjusted_dmg += self.owner.str
                self.dmg = adjusted_dmg

            elif fighting_style == True and roll == 20:
                adjusted_dmg = 0
                for _ in range(2*self.number):
                    dmg_roll = max(rd.randint(1, self.dice_type), 3)
                    adjusted_dmg += dmg_roll
                adjusted_dmg +=  self.owner.str
                self.dmg = adjusted_dmg

        if self.dmg == 0 and mastery == True:
            self.dmg = self.owner.str

        return hit, roll, self.dmg

    def simulate_attacks(self, num_attacks=1000):
        print("Enter attack details:")
        attack_inputs = AttackHandler.get_attack_inputs()  # Collect user inputs

        total_damage = 0
        total_hit_damage = 0
        hit_count = 0
        results = []

        for _ in range(num_attacks):
            hit, roll, damage = self.perform_attack(
                ac=attack_inputs['ac'],
                dex=attack_inputs['dex'],
                advantage=attack_inputs['advantage'],
                disadvantage=attack_inputs['disadvantage'],
                mastery=attack_inputs['mastery'],
                fighting_style=attack_inputs['fighting_style'],
            )
            results.append(damage)
            total_damage += damage
            if hit:
                total_hit_damage += damage
                hit_count += 1

        print("Unique Damage Values:", set(results))

        overall_avg_damage = total_damage / num_attacks
        hit_avg_damage = total_hit_damage / hit_count if hit_count > 0 else 0

        return results, overall_avg_damage, hit_avg_damage, hit_count, total_hit_damage

    def __str__(self):
        return f"You Greatsword deals {self.dmg} damage to the target!"

