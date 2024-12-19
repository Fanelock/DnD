from Greatsword import Greatsword
from Longbow import Longbow
from Shortsword import Shortsword
from Dagger import Dagger
from Sneak_attack import SneakAttack
from Ranger_class import Ranger
from Rogue_class import Rogue
from Attack import AttackHandler
from create_character import Create

#Create a Character:
#Name = Class(str_mod, dex_mod, wis_mod, prof_bonus) -> in rogues Rogue(str, dex, prof, sneak_dice_number, sneak_dice_type)
#
#Create Weapon Instance:
#Name_Weapon = Weapon(Name, number of dice, type of dice)
#
#Execute Attack:
#Name_weapon_dmg = AttackHandler.perform_attack(Name_Weapon, Name)
#will open console -> ask for the following inputs: AC, if dex/str should be used for the attack, adv/disadvantage, mastery & fighting style

#Fane = Ranger(3, 2, 3, 2)

create = Create(r'C:\Users\colin\OneDrive\Desktop\DnD 2.0\Fane.xlsx')
create.read()

# Access a specific character by name
Fane = create.get_character("Fane")

Fane_Greatsword = Greatsword(Fane, 2, 6)
#Fane_Longbow = Longbow(Fane, 1, 8)

Fane_Greatsword_dmg = AttackHandler.perform_attack(Fane_Greatsword, Fane)
#Fane_Longbow_dmg = AttackHandler.perform_attack(Fane_Longbow, Fane)

print(Fane_Greatsword)
#print(Fane_Longbow)

Catto = Rogue(1,4,2, 2, 6)

Catto_Shortsword = Shortsword(Catto, 1, 6)
Catto_Dagger = Dagger(Catto, 1, 4)
sneak_attack = SneakAttack(Catto, 2, 6)

#Catto_Shortsword_dmg = AttackHandler.perform_attack(Catto_Shortsword, Catto)
#Catto_dagger_dmg = AttackHandler.perform_attack(Catto_Dagger, Catto)

print(Catto_Shortsword)
print(Catto_Dagger)




