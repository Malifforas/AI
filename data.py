from pokeapi import PokeAPI

poke_api = PokeAPI()

# Get a list of all available Pokemon
all_pokemon = poke_api.get_all_pokemon()

# Create a dictionary to map move names to their IDs
move_dict = {}
for move in poke_api.get_all_moves():
    move_dict[move['name']] = move['id']

# Create a dictionary to map type names to their IDs
type_dict = {}
for poke_type in poke_api.get_all_types():
    type_dict[poke_type['name']] = poke_type['id']

# Create a dictionary to map ability names to their IDs
ability_dict = {}
for ability in poke_api.get_all_abilities():
    ability_dict[ability['name']] = ability['id']

# Create a dictionary to map item names to their IDs
item_dict = {}
for item in poke_api.get_all_items():
    item_dict[item['name']] = item['id']

# Create a dictionary to map stat names to their IDs
stat_dict = {}
for stat in poke_api.get_all_stats():
    stat_dict[stat['name']] = stat['id']

# Create a dictionary to map nature names to their IDs
nature_dict = {}
for nature in poke_api.get_all_natures():
    nature_dict[nature['name']] = nature['id']