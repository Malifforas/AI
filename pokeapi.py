from pokeapi import PokeAPI as API


class PokeAPI:
    def __init__(self):
        self.api = API()

    def get_pokemon(self, name):
        pokemon = self.api.get_pokemon(name)
        return {
            'name': pokemon.name,
            'type': [t.type.name for t in pokemon.types],
            'stats': {s.stat.name: s.base_stat for s in pokemon.stats},
            'moves': [m.move.name for m in pokemon.moves]
        }