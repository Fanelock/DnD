import random as rd
from abc import ABC, abstractmethod

class weapon_attack(ABC):
    def __init__(self, str_mod, dex_mod, prof_bonus):
        self.str = str_mod
        self.dex = dex_mod
        self.prof = prof_bonus
        self.hit_roll = 0
        self.dmg = 0

    def attack_roll(self, ac, dex, advantage, disadvantage):
        if advantage:
            hit_roll_1 = rd.randint(1,20)
            hit_roll_2 = rd.randint(1,20)
            print(hit_roll_1, hit_roll_2)
            self.hit_roll = max(hit_roll_1, hit_roll_2)
        elif disadvantage:
            hit_roll_1 = rd.randint(1, 20)
            hit_roll_2 = rd.randint(1, 20)
            print(hit_roll_1, hit_roll_2)
            self.hit_roll = min(hit_roll_1, hit_roll_2)
        else:
            self.hit_roll = rd.randint(1, 20)
            print(self.hit_roll)
        if dex:
            total = self.hit_roll + self.dex + self.prof
        else:
            total = self.hit_roll + self.str + self.prof

        return total >= ac, self.hit_roll, advantage


weapon = weapon_attack(2, 3, 2)  # Using str_mod=2, dex_mod=3, prof_bonus=2

# Assume the target's AC is 15
ac = 15

# Regular attack (no advantage, no disadvantage)
hit, roll, advantage = weapon.attack_roll(ac, True, False, False)
print(f"Regular Attack: Hit = {hit}, Roll = {roll}, Advantage = {advantage}")

# Advantage attack (roll twice, take the higher)
hit, roll, advantage = weapon.attack_roll(ac, True, True, False)
print(f"Advantage Attack: Hit = {hit}, Roll = {roll}, Advantage = {advantage}")

# Disadvantage attack (roll twice, take the lower)
hit, roll, advantage = weapon.attack_roll(ac, True, False, True)
print(f"Disadvantage Attack: Hit = {hit}, Roll = {roll}, Advantage = {advantage}")