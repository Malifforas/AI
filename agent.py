import random
import numpy as np
import os.path
import json

class Agent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_rate=0.99, epsilon=1.0, min_epsilon=0.01,
                 epsilon_decay_rate=0.001, q_table_path=None):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = epsilon
        self.min_epsilon = min_epsilon
        self.epsilon_decay_rate = epsilon_decay_rate
        self.q_table_path = q_table_path
        self.q_table = self.load_q_table(q_table_path)

    def get_action(self, state, valid_actions):
        if np.random.rand() < self.epsilon:
            return random.choice(valid_actions)
        else:
            q_values = self.q_table.get(str(state), np.zeros(self.action_size))
            max_q_value = np.max(q_values)
            indices = np.where(q_values == max_q_value)[0]
            if len(indices) == 1:
                return valid_actions[indices[0]]
            else:
                return valid_actions[random.choice(indices)]

    def update_q_table(self, state, action, next_state, reward):
        q_values = self.q_table.get(str(state), np.zeros(self.action_size))
        next_q_values = self.q_table.get(str(next_state), np.zeros(self.action_size))
        next_max_q_value = np.max(next_q_values)
        td_target = reward + self.discount_rate * next_max_q_value
        td_error = td_target - q_values[action]
        q_values[action] += self.learning_rate * td_error
        self.q_table[str(state)] = q_values

    def decay_epsilon(self):
        self.epsilon = max(self.min_epsilon, self.epsilon - self.epsilon_decay_rate)

    def save_q_table(self):
        if self.q_table_path is not None:
            with open(self.q_table_path, 'w') as f:
                json.dump(self.q_table, f)

    def load_q_table(self, q_table_path):
        if q_table_path is not None and os.path.isfile(q_table_path):
            with open(q_table_path, 'r') as f:
                q_table = json.load(f)
                for key in q_table.keys():
                    q_table[key] = np.array(q_table[key])
            return q_table
        else:
            return {}