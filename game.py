import json
import os


class Game:
    def __init__(self, rom_path):
        self.rom_path = rom_path
        self.data_dir = os.path.join(os.getcwd(), "pokegold-master", "data")
        self.moves = self.load_moves()
        self.types = self.load_types()
        self.pokemon = self.load_pokemon()

    def load_moves(self):
        with open(os.path.join(self.data_dir, 'moves.json')) as f:
            moves = json.load(f)
        return moves

    def load_types(self):
        with open(os.path.join(self.data_dir, 'types.json')) as f:
            types = json.load(f)
        return types

    def load_pokemon(self):
        with open(os.path.join(self.data_dir, 'pokemon.json')) as f:
            pokemon = json.load(f)
        return pokemon