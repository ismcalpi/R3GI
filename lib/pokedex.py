import json

with open('./lib/pokedex.json', 'r') as f:
    pokedex_json = json.load(f)


class Team:
    def __init__(self, config):
        with open(config) as c:
            config_json = json.load(config)

        self.members = []
        for key in config_json.keys():
            self.members.append(Pokemon(key['name'], key['logic'], key['moveset']))


class Move:
    def __init__(self, lookup, owner):
        self.id = pokedex_json['moves'][lookup]['id']
        self.name = pokedex_json['moves'][lookup]['name']
        self.type = pokedex_json['moves'][lookup]['type']
        self.category = pokedex_json['moves'][lookup]['category']
        self.pp = pokedex_json['moves'][lookup]['pp']
        self.power = pokedex_json['moves'][lookup]['power']
        self.accuracy = pokedex_json['moves'][lookup]['accuracy']
        if self.type in owner.type:
            self.stab = 1.5
        else:
            self.stab = 1

    def damage(self, opponent):
        mod = opponent.effective[self.type] * self.stab
        dmg = (((22 * self.power) / 50) + 2) * mod
        return round(dmg, 0)

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
    def __init__(self, lookup, logic=None, moveset=None):
        self.id = pokedex_json['pokemon'][lookup]['id']
        self.name = pokedex_json['pokemon'][lookup]['name']
        self.type = pokedex_json['pokemon'][lookup]['type']
        self.ability = pokedex_json['pokemon'][lookup]['ability']
        self.effective = pokedex_json['pokemon'][lookup]['effective']
        if logic is not None:
            self.logic = logic
        if moveset is not None:
            self.moveset = []
            for move in moveset:
                self.moveset.append(Move(move, self))

    def get_best_move(self, opponent):
        dmg = []
        for move in self.moveset:
            dmg.append(move.damage(opponent))
        return self.moveset[dmg.index(max(dmg))]

    def get_max_dmg(self, opponent):
        dmg = []
        for move in self.moveset:
            dmg.append(move.damage(opponent))
        return max(dmg)

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
        if self.moveset is not None:
            for move in self.moveset:
                move.print_output()
