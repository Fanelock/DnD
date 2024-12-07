from abc import ABC, abstractmethod
from Sneak_attack import SneakAttack

class Rogue(ABC):
    def __init__(self, str_mod, dex_mod, prof_bonus, sneak_dice, sneak_type):
        self.str = str_mod
        self.dex = dex_mod
        self.prof = prof_bonus
        self.sneak_attack_handler = SneakAttack(self, sneak_dice, sneak_type)

    def attack(self, dex, advantage, disadvantage, mastery, fighting_style):
        pass

    def perform_sneak_attack(self, hit, advantage):
        if hit and advantage:
            return self.sneak_attack_handler.sneak_damage()
        return 0

