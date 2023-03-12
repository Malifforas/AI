import time
import subprocess
import pyautogui
import numpy as np
import cv2


class Emulator:
    def __init__(self, emulator_path, rom_path):
        self.emulator_path = emulator_path
        self.rom_path = rom_path
        self.proc = None
        self.screen = None

    def start(self):
        self.proc = subprocess.Popen([self.emulator_path, self.rom_path])

        # Wait for emulator to start up
        time.sleep(5)

    def get_screen(self):
        # Capture screenshot of emulator window
        screen = pyautogui.screenshot(region=(0, 0, 640, 480))

        # Convert screenshot to numpy array and resize
        screen = np.array(screen)
        screen = cv2.resize(screen, (84, 84))

        # Convert BGR to RGB
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

        # Save a copy of the screen
        self.screen = screen.copy()

        # Normalize pixel values to be between 0 and 1
        screen = screen / 255.0

        return screen

    def press_button(self, button):
        button_map = {
            "UP": "up",
            "DOWN": "down",
            "LEFT": "left",
            "RIGHT": "right",
            "A": "z",
            "B": "x",
            "START": "enter",
            "SELECT": "backspace"
        }

        if button in button_map:
            pyautogui.press(button_map[button])
        else:
            raise ValueError(f"Invalid button: {button}")

    def stop(self):
        if self.proc:
            self.proc.kill()