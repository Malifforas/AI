import os
import json

data_dir = r'C:\Users\Blizzard\Desktop\AI\pokegold-master'

with open(os.path.join(data_dir, 'moves.json')) as f:
    moves = json.load(f)

with open(os.path.join(data_dir, 'types.json')) as f:
    types = json.load(f)

with open(os.path.join(data_dir, 'pokemon.json')) as f:
    pokemon = json.load(f) 