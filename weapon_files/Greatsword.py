import random as rd
from .. import AttackHandler
from ..Weapon_main import WeaponAttack

class Greatsword(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, "Greatsword", "Two-Handed")
        self.number = 2
        self.dice_type = 6
        self.dmg = 0
        self.supports_sneak_attack = False

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack=None):
        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        self.dmg = self.apply_fighting_style(hit, roll, self.number, self.dice_type, dex)

        if self.dmg == 0 and mastery == True:
            self.dmg = self.owner.str

        return hit, roll, self.dmg

    def simulate_attacks(self, num_attacks=1000):
        print("Enter attack details:")
        attack_inputs = AttackHandler.get_attack_inputs()  # Collect user inputs

        include_crits = input("Include critical hits in the simulation? (1/0): ").strip().lower() == '1'

        total_damage = 0
        total_hit_damage = 0
        hit_count = 0
        results = []

        for _ in range(num_attacks):
            while True:
                hit, roll, damage = self.perform_attack(
                    ac=attack_inputs['ac'],
                    dex=attack_inputs['dex'],
                    advantage=attack_inputs['advantage'],
                    disadvantage=attack_inputs['disadvantage'],
                    mastery=attack_inputs['mastery'],
                    fighting_style=self.owner.fighting_style,
                )
                if include_crits or roll != 20:  # If crits are allowed, or this is not a crit, exit the loop
                    break
            results.append(damage)
            total_damage += damage
            if hit:
                total_hit_damage += damage
                hit_count += 1

        overall_avg_damage = total_damage / num_attacks
        hit_avg_damage = total_hit_damage / hit_count if hit_count > 0 else 0

        return results, overall_avg_damage, hit_avg_damage, hit_count, total_hit_damage

    def __str__(self):
        return f"You Greatsword deals {self.dmg} damage to the target!"

