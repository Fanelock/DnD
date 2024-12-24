from ..Weapon_main import WeaponAttack
from ..class_files import SneakAttack
from ..class_files import Rogue
from .. import AttackHandler

class Shortsword(WeaponAttack):
    def __init__(self, owner):
        super().__init__(owner, "Shortsword", "Light")
        self.number = 1
        self.dice_type = 6
        self.dmg = 0
        self.supports_sneak_attack = True
        self.attack_counter = 1

    def perform_attack(self, ac, dex, advantage, disadvantage, mastery, fighting_style, sneak_attack: SneakAttack = None):
        if mastery:
            advantage = self.attack_counter % 2 == 0

        hit, roll, advantage = super().attack_roll(ac, dex, advantage, disadvantage)

        self.dmg = self.calc_dmg(hit, roll, self.number, self.dice_type, dex)

        self.dmg = self.apply_fighting_style(hit, roll, self.number, self.dice_type, dex)

        if isinstance(self.owner, Rogue):
            sneak_dmg = self.owner.perform_sneak_attack(hit, advantage, roll)
            self.dmg += sneak_dmg

        self.attack_counter += 1

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
        return f"You Shortsword deals {self.dmg} damage to the target!"