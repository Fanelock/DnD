from abc import ABC, abstractmethod

class Ranger(ABC):
    def __init__(self, str_mod, dex_mod, wis_mod, prof_bonus):
        self.str = str_mod
        self.dex = dex_mod
        self.wis = wis_mod
        self.prof = prof_bonus

    def attack(self, dex, advantage, disadvantage, mastery, fighting_style):
        pass
