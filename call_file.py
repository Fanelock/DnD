from DND_weapons.weapon_files import Shortsword, Dagger, Greatsword, Longbow, Longsword, Glaive, Flintlock
from DND_weapons.class_files import Rogue, Ranger
from Attack import AttackHandler
from create_character import Create
import matplotlib.pyplot as plt

#Create a Character:
#create = Create(r'file-path')
#create.read()
#Character_name = create.get_character("Name") %"Name" -> named of character specified in excel sheet
#
#Create Weapon Instance:
#Name_Weapon = Weapon(Character_Name)
#
#Execute Attack:
#Name_weapon_dmg = AttackHandler.perform_attack(Name_Weapon, Name)
#will open console -> ask for the following inputs: AC, if dex/str should be used for the attack, adv/disadvantage & mastery

create = Create(r'Path')
create.read()

# Access a specific character by name
Fane = create.get_character("Fane")
Catto = create.get_character("Catto")

Fane_Greatsword = Greatsword(Fane)

Catto_Shortsword = Shortsword(Catto)

#Fane_Longbow_dmg = AttackHandler.perform_attack(Fane_Longbow, Fane)

#print(Fane_Longbow)

#Catto = Rogue(1,"Thief",2, 2, 1, 1, 3, 2, 2)


#Catto_Dagger = Dagger(Catto)


#Catto_Shortsword_dmg = AttackHandler.perform_attack(Catto_Shortsword, Catto)
#Catto_dagger_dmg = AttackHandler.perform_attack(Catto_Dagger, Catto)

#print(Catto_Shortsword)
#print(Catto_Dagger)

damage_results, avg_damage, avg_hit_damage, hit_count, total_hit_damage = Fane_Greatsword.simulate_attacks(num_attacks=1000)
print("Average Damage:", avg_damage)
print("Average Damage on Hit:", avg_hit_damage)
print("Total Hits:", hit_count)
print("Total Hit Damage:", total_hit_damage)

def plot_damage_distribution(damage_results):
    if not damage_results:
        print("No damage results to plot.")
        return

    min_damage = min(damage_results)
    max_damage = max(damage_results)

    if min_damage == max_damage:
        bins = [min_damage - 1, min_damage, min_damage + 1]
    else:
        bins = range(min_damage, max_damage + 2)

    plt.hist(damage_results, bins=bins, align='left', color='violet', alpha=0.7)
    plt.xlabel('Damage')
    plt.ylabel('Frequency')
    plt.title('Damage Distribution over 1000 Attacks')
    plt.xticks(range(min(bins), max(bins) + 1, max(1, len(bins) // 20)), rotation=45, fontsize=8)
    plt.grid(axis='y')
    plt.show()

plot_damage_distribution(damage_results)

damage_results_2, avg_damage_2, avg_hit_damage_2, hit_count_2, total_hit_damage_2 = Catto_Shortsword.simulate_attacks(num_attacks=1000)
print("Average Damage:", avg_damage_2)
print("Average Damage on Hit:", avg_hit_damage_2)
print("Total Hits:", hit_count_2)
print("Total Hit Damage:", total_hit_damage_2)

def plot_damage_distribution(damage_results):
    if not damage_results:
        print("No damage results to plot.")
        return

    min_damage = min(damage_results)
    max_damage = max(damage_results)

    if min_damage == max_damage:
        bins = [min_damage - 1, min_damage, min_damage + 1]
    else:
        bins = range(min_damage, max_damage + 2)

    plt.hist(damage_results, bins=bins, align='left', color='violet', alpha=0.7)
    plt.xlabel('Damage')
    plt.ylabel('Frequency')
    plt.title('Damage Distribution over 1000 Attacks')
    plt.xticks(range(min(bins), max(bins) + 1, max(1, len(bins) // 20)), rotation=45, fontsize=8)
    plt.grid(axis='y')
    plt.show()

plot_damage_distribution(damage_results_2)
