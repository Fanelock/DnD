from abc import ABC, abstractmethod

class Ranger(ABC):
    def __init__(self, level, subclass, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, prof_bonus):
        self.level = level
        self.subclass = subclass
        self.str = str_mod
        self.dex = dex_mod
        self.con = con_mod
        self.int = int_mod
        self.wis = wis_mod
        self.cha = cha_mod
        self.prof = prof_bonus

    def attack(self, dex, advantage, disadvantage, mastery, fighting_style):
        pass

