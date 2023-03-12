import random


class Agent:
    def __init__(self):
        self.q_table = {}

    def get_action(self, state, valid_actions):
        action = random.choice(valid_actions)
        return action

    def update_q_table(self, state, action, next_state, reward):
        pass
