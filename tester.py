from lib import pokedex as dex

opponent = dex.Pokemon('vileplume')
ally = dex.Pokemon('dragonite', None, ["dragonclaw", "firepunch", "fly", "earthquake"])

print(f"Ally {ally.name} deals the most damage to {opponent.name} with {ally.get_best_move(opponent).name} which deals {ally.get_best_move(opponent).damage(opponent)} damage")