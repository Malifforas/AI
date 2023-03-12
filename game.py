import json
import os
import cv2
from datetime import datetime
from emulator import Emulator


class Game:
    def __init__(self, rom_path):
        self.emulator = Emulator(rom_path)
        self.screen = None

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