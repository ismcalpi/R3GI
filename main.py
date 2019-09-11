from lib import pokedex
import logging

log = logging.getLogger("my-logger")

opponent = pokedex.Pokemon('dragonite')
ally = pokedex.Pokemon('dragonite', moveset=["dragonclaw", "firepunch", "fly", "earthquake"])

