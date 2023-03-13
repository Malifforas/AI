import time
import pyautogui

def press_key(key):
    pyautogui.keyDown(key)
    time.sleep(0.05)
    pyautogui.keyUp(key)

class EmulatorInteraction:
    def __init__(self):
        pass

    def start_game(self):
        press_key('enter')
        time.sleep(2)
        press_key('z')
        time.sleep(2)
        press_key('z')
        time.sleep(10)

    def press_button(self, button):
        if button == 'A':
            press_key('x')
        elif button == 'B':
            press_key('z')
        elif button == 'UP':
            press_key('up')
        elif button == 'DOWN':
            press_key('down')
        elif button == 'LEFT':
            press_key('left')
        elif button == 'RIGHT':
            press_key('right')
        time.sleep(0.1)