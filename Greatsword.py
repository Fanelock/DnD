#avg damage output

import random as rd
import matplotlib.pyplot as plt

class Greatsword:
    def __init__(self, str_mod, prof):
        self.str_mod = str_mod
        self.prof = prof
        self.dmg = 0
        self.hit_roll = 0

    def to_hit(self, ac):
        self.hit_roll = rd.randint(1,20)
        total = self.hit_roll + self.str_mod + self.prof
        return total >= ac

    def calc_dmg(self, hit):
        if not hit:
            self.dmg = self.str_mod
            return self.dmg
        else:
            dmg_roll_1 = max(rd.randint(1, 6), 3)
            dmg_roll_2 = max(rd.randint(1, 6), 3)
            self.dmg = dmg_roll_1 + dmg_roll_2 + self.str_mod
        return self.dmg

    def __str__(self):
        return f"The attack deals {self.dmg} damage to the target!"

    def simulate_attacks(self, ac, num_attacks=1000):
        total_damage = 0
        total_hit_damage = 0
        hit_count = 0
        results = []

        for _ in range(num_attacks):
            hit = self.to_hit(ac)
            damage = self.calc_dmg(hit)
            results.append(damage)
            total_damage += damage
            if hit:
                total_hit_damage += damage
                hit_count += 1

        overall_avg_damage = total_damage / num_attacks
        hit_avg_damage = total_hit_damage / hit_count if hit_count > 0 else 0

        return results, overall_avg_damage, hit_avg_damage

ranger = Greatsword(3, 2)
hit = ranger.to_hit(15)
dmg = ranger.calc_dmg(hit)
print(ranger)

def plot_damage_distribution(damage_results):
    plt.hist(damage_results, bins=range(min(damage_results), max(damage_results) + 2), align='left', color='violet', alpha=0.7)
    plt.xlabel('Damage')
    plt.ylabel('Frequency')
    plt.title('Damage Distribution over 1000 Attacks')
    plt.xticks(range(min(damage_results), max(damage_results) + 1))
    plt.grid(axis='y')
    plt.show()

ranger = Greatsword(3, 2)
damage_results, average_damage, average_hit_damage = ranger.simulate_attacks(15)

print(f"Overall average damage over 1000 attacks (including misses): {average_damage:.2f}")
print(f"Average damage for successful hits only: {average_hit_damage:.2f}")

plot_damage_distribution(damage_results)