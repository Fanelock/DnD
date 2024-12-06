from Greatsword import Greatsword
from Longbow import Longbow
from Shortsword import Shortsword
from Dagger import Dagger
from Weapon_main import weapon_attack
from Sneak_attack import Sneak_attack

ranger_greatsword = Greatsword(3, 2, 2, 2, 6)
ranger_longbow = Longbow(3, 2, 2, 1, 8)


rogue_shortsword = Shortsword(1, 4, 3, 1, 6)
rogue_dagger = Dagger(1, 4, 2, 1, 4)
sneak_attack = Sneak_attack(1, 4, 2, 2, 6)

ranger_longbow_dmg = ranger_longbow.perform_attack(15, True, False, False, False, False)
ranger_greatsword_dmg = ranger_greatsword.perform_attack(15, False, False, False, True, True)

rogue_shortsword_dmg = rogue_shortsword.perform_attack(15, True, True, False, False, False, sneak_attack)
rogue_dagger_dmg = rogue_dagger.perform_attack(15, True, True, False, True, False, sneak_attack)

print(ranger_greatsword)
print(ranger_longbow)
print(rogue_shortsword)
print(rogue_dagger)




