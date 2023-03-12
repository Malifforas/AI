import random

class QLearningAgent:
    def __init__(self, learning_rate, discount_factor, exploration_rate):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = {}

    def update_q_table(self, state, action, reward, next_state):
        pass

    def choose_action(self, state):
        pass

    def get_best_action(self, state):
        pass
