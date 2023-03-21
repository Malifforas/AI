import os
import pickle
import random
from collections import defaultdict

from game import Game
import numpy as np



class QLearningAgent:
    def __init__(self, alpha=0.5, gamma=0.99, epsilon=1.0, epsilon_decay=0.9999, min_epsilon=0.01, actions=None):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.q_table = defaultdict(lambda: np.zeros(len(actions))) if actions is not None else {}
        self.actions = actions or []
        self.q_table = defaultdict(lambda: [0.0] * len(self.actions))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            # Choose a random action
            return random.choice(self.actions)
        else:
            # Choose the best action based on the Q-table
            return self.actions[self.q_table[state].index(max(self.q_table[state]))]

    def update_q_table(self, state, action, reward, next_state, done):
        # Update Q-value of the state-action pair using the Q-learning update rule
        current_q = self.q_table[state][action]
        if done:
            # If the game is over, the next max Q-value is 0
            next_max_q = 0
        else:
            # Otherwise, use the max Q-value of the next state
            next_max_q = max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * next_max_q - current_q)
        self.q_table[state][action] = new_q

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

    def save_q_table(self, file_path):
        full_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'AI', 'qtable', file_path)
        with open(full_path, 'wb') as f:
            pickle.dump(dict(self.q_table), f)

    def load_q_table(self, file_path):
        full_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'AI', 'qtable', file_path)
        with open(full_path, 'rb') as f:
            self.q_table = defaultdict(lambda: [0.0] * len(self.actions), pickle.load(f))



class QLearning:
    def __init__(self, game: Game):
        self.game = game
        self.agent = QLearningAgent(game.get_actions())
        self.num_episodes = 1000

    def train(self):
        for i in range(self.num_episodes):
            self.game.start()
            state = self.game.get_state()
            done = False
            while not done:
                action = self.agent.choose_action(state)
                self.game.take_action(action)
                next_state = self.game.get_state()
                reward = self.game.get_reward()
                self.agent.update_q_table(state, action, reward, next_state)
                state = next_state
                if self.game.game_over:
                    done = True
                    break
            self.agent.decay_epsilon()

    def play(self):
        self.game.start()
        state = self.game.get_state()
        while not self.game.game_over:
            action = self.agent.choose_action(state)
            self.game.take_action(action)
            state = self.game.get_state()
    def save_q_table(self, file_path):
        self.agent.save_q_table(file_path)

    def load_q_table(self, file_path):
        self.agent.load_q_table(file_path)