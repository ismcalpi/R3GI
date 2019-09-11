import json

with open('pokedex.json', 'r') as f:
    pokedex_json = json.load(f)


class Move:
    def __init__(self, lookup):
        self.id = pokedex_json['moves'][lookup]['id']
        self.name = pokedex_json['moves'][lookup]['name']
        self.type = pokedex_json['moves'][lookup]['type']
        self.category = pokedex_json['moves'][lookup]['category']
        self.pp = pokedex_json['moves'][lookup]['pp']
        self.power = pokedex_json['moves'][lookup]['power']
        self.accuracy = pokedex_json['moves'][lookup]['accuracy']

    def print_output(self):
        print("")
        print("Move Object Output")
        print("------------------")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Type: {self.type}")
        print(f"PP: {self.pp}")
        print(f"Power: {self.power}")
        print(f"Accuracy: {self.accuracy}")
        print("------------------")


class Pokemon:
    def __init__(self, lookup, moveset=None):
        self.id = pokedex_json['pokemon'][lookup]['id']
        self.name = pokedex_json['pokemon'][lookup]['name']
        self.type = pokedex_json['pokemon'][lookup]['type']
        self.ability = pokedex_json['pokemon'][lookup]['ability']
        self.effective = pokedex_json['pokemon'][lookup]['effective']

        if isinstance(moveset, list):
            self.moves = []
            for num, name in enumerate(moveset):
                tmp_move = Move(name)
                self.moves.append(tmp_move)

    def print_output(self):
        print("Pokemon Object Output")
        print("------------------")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Type(s): {', '.join(self.type)}")
        print(f"Ability(s): {', '.join(self.ability)}")
        print("Type Effectiveness")
        for k, v in self.effective.items():
            print(f"    {k} = {v}")
        if isinstance(self.moves, list):
            for i in self.moves:
                i.print_output()
