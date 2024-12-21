from abc import ABC, abstractmethod
from .Sneak_attack import SneakAttack

class Rogue(ABC):
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
        self.sneak_attack_handler = SneakAttack(self)

    def attack(self, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def perform_sneak_attack(self, hit, advantage):
        if hit and advantage:
            return self.sneak_attack_handler.sneak_damage()
        return 0

