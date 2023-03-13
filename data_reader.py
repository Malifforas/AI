import json
import os


class DataReader:
    def __init__(self):
        self.ROOT_DIR = os.path.abspath(os.curdir)
        self.POKEDEX = self.read_json_file('pokedex.json')
        self.MOVES = self.read_json_file('moves.json')
        self.TYPE_CHART = self.read_json_file('type_chart.json')
        self.GYM_LEADERS = self.read_json_file('gym_leaders.json')
        self.ELITE_FOUR = self.read_json_file('elite_four.json')
        self.CHAMPION = self.read_json_file('champion.json')
        self.LEVEL_LIMITS = self.read_json_file('level_limits.json')

    def read_json_file(self, filename):
        filepath = os.path.join(self.ROOT_DIR, 'data', filename)
        with open(filepath, 'r') as f:
            return json.load(f)

    def get_pokemon_by_id(self, pokemon_id):
        return self.POKEDEX[str(pokemon_id)]

    def get_pokemon_by_name(self, name):
        for pokemon in self.POKEDEX.values():
            if pokemon['name'].lower() == name.lower():
                return pokemon
        return None

    def get_move_by_id(self, move_id):
        return self.MOVES[str(move_id)]

    def get_gym_leader_by_id(self, gym_leader_id):
        return self.GYM_LEADERS[str(gym_leader_id)]

    def get_elite_four_member_by_id(self, elite_four_member_id):
        return self.ELITE_FOUR[str(elite_four_member_id)]

    def get_champion(self):
        return self.CHAMPION

    def get_level_limit_for_gym(self, gym_name):
        if gym_name.lower() in self.LEVEL_LIMITS:
            return self.LEVEL_LIMITS[gym_name.lower()]
        return None

    def get_type_chart(self):
        return self.TYPE_CHART