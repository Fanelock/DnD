from Greatsword import Greatsword
from Longbow import Longbow

ranger_greatsword = Greatsword(3, 2, 2, 2, 6)
ranger_longbow = Longbow(3, 2, 2, 1, 8)

ranger_longbow_dmg = ranger_longbow.perform_attack(15, True, False, False)
ranger_greatsword_dmg = ranger_greatsword.perform_attack(15, False, True, True)

print(ranger_greatsword)
print(ranger_longbow)





