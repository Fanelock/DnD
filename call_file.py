from Greatsword import Greatsword
from Longbow import Longbow
from Shortsword import Shortsword
from Dagger import Dagger
from Sneak_attack import SneakAttack
from Ranger_class import Ranger
from Rogue_class import Rogue
from Attack import AttackHandler

Fane = Ranger(3, 2, 3, 2)

Fane_Greatsword = Greatsword(Fane, 2, 6)
Fane_Longbow = Longbow(Fane, 1, 8)

Fane_Greatsword_dmg = Fane_Greatsword.perform_attack(15, False, False, False, True, True)
Fane_Longbow_dmg = Fane_Longbow.perform_attack(15, True, False, False, False, False)

print(Fane_Greatsword)
print(Fane_Longbow)

Catto = Rogue(1,4,2, 2, 6)

Catto_Shortsword = Shortsword(Catto, 1, 6)
Catto_Dagger = Dagger(Catto, 1, 4)
sneak_attack = SneakAttack(Catto, 2, 6)

Catto_Shortsword_dmg = AttackHandler.perform_attack(Catto_Shortsword, Catto)
Catto_dagger_dmg = AttackHandler.perform_attack(Catto_Dagger, Catto)

print(Catto_Shortsword)
print(Catto_Dagger)




