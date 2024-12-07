import random as rd
from abc import ABC, abstractmethod

class Weapon_attack(ABC):
    def __init__(self, owner):
        self.owner = owner
        self.hit_roll = 0
        self.dmg = 0

    def attack_roll(self, ac, dex, advantage, disadvantage):
        if advantage:
            hit_roll_1 = rd.randint(1,20)
            hit_roll_2 = rd.randint(1,20)
            self.hit_roll = max(hit_roll_1, hit_roll_2)
        elif disadvantage:
            hit_roll_1 = rd.randint(1, 20)
            hit_roll_2 = rd.randint(1, 20)
            self.hit_roll = min(hit_roll_1, hit_roll_2)
        else:
            self.hit_roll = rd.randint(1, 20)
        if dex:
            total = self.hit_roll + self.owner.dex + self.owner.prof
        else:
            total = self.hit_roll + self.owner.str + self.owner.prof

        return total >= ac, self.hit_roll, advantage

    def calc_dmg(self, hit, roll, number, dice_type, dex):
        self.dmg = 0
        if roll == 20:
            for i in range(2 * number):
                dmg_roll = rd.randint(1, dice_type)
                self.dmg += dmg_roll
            self.dmg += self.owner.dex if dex else self.owner.str
            return self.dmg
        elif not hit:
            return self.dmg
        else:
            for i in range(number):
                dmg_roll = rd.randint(1, dice_type)
                self.dmg += dmg_roll
            self.dmg += self.owner.dex if dex else self.owner.str
        return self.dmg

    @abstractmethod
    def __str__(self):
        pass

