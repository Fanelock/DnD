from email.policy import default

import pandas as pd
from DND_weapons.class_files import Ranger, Rogue

class Create:
    def __init__(self, file):
        self.file = file
        self.characters = {}

    def read(self):
        data = pd.read_excel(self.file)

        for _, row in data.iterrows():
            name = row['Name']
            level = int(row['Level'])
            class_name = row['Class']
            subclass_name = row.get('Subclass', None)
            fighting_style = row.get('Fighting Style', None)
            str_mod = int(row['Str'])
            dex_mod = int(row['Dex'])
            con_mod = int(row['Con'])
            int_mod = int(row['Int'])
            wis_mod = int(row['Wis'])
            cha_mod = int(row['Cha'])
            prof_bonus = int(row['Prof'])

            class_ = globals().get(class_name)

            if class_:
                if class_name == "Ranger":
                    character = class_(level, subclass_name, fighting_style, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, prof_bonus)
                elif class_name == "Rogue":
                    character = class_(level, subclass_name,fighting_style, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, prof_bonus)
                else:
                    print(f"Unsupported class: {class_name}")
                    continue

                character.name = name
                self.characters[name] = character
            else:
                print(f"Class {class_name} not found for {name}!")

    def get_character(self, name):
        return self.characters.get(name)

    def print_all_characters(self):
        if not self.characters:
            print("No characters have been created.")
        for name, character in self.characters.items():
            print(
                f"Character created: {character.name} as {character.__class__.__name__} with subclass: {getattr(character, 'subclass', 'N/A')}")



