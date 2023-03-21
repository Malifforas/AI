import json
import os
import cv2
from datetime import datetime
from emulator import Emulator


class Game:
    def __init__(self, rom_path):
        self.emulator = Emulator(rom_path)
        self.screen = None
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.moves = self.load_moves()
        self.types = self.load_types()
        self.pokemon = self.load_pokemon()
        self.score = 0

    def start(self):
        self.emulator.start()
        self.emulator.press_button("START")
        self.emulator.press_button("A")
        self.emulator.press_button("B")

    def take_screenshot(self):
        self.screen = self.emulator.get_screen()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'AI', 'screenshots', f"screenshot_{timestamp}.png")
        cv2.imwrite(screenshot_path, self.screen)

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

    def calculate_reward(self, state, action, next_state, done):
        reward = 0
        if done:
            if self.score >= 3000:
                reward = 1000
            elif self.score >= 2000:
                reward = 500
            elif self.score >= 1000:
                reward = 100
        else:
            if next_state["player"]["pokemon"]:
                pokemon_hp = next_state["player"]["pokemon"][0]["current_hp"]
                if pokemon_hp < state["player"]["pokemon"][0]["current_hp"]:
                    reward += 50
                if pokemon_hp == 0:
                    reward -= 500
                    self.score += 100
            if action == "FIGHT":
                if next_state["opponent"]["pokemon"][0]["current_hp"] == 0:
                    reward += 200
            if action == "RUN":
                reward -= 50
        self.score += reward
        return reward