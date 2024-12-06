#from Weapon_main import weapon_attack
from Greatsword import Greatsword
from Longbow import Longbow

ranger_greatsword = Greatsword(3, 2, 2)
ranger_longbow = Longbow(3, 2, 2)

ranger_hit_str = ranger_greatsword.attack_roll(15, False)  # Using Strength for attack
ranger_hit_dex = ranger_greatsword.attack_roll(15, True)  # Using Dexterity for attack

# Calculate damage for both hit scenarios
ranger_greatsword_dmg = ranger_greatsword.calc_dmg(ranger_hit_str)
ranger_longbow_dmg = ranger_longbow.calc_dmg(ranger_hit_dex)

print(ranger_greatsword)
print(ranger_longbow)



