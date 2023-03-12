import os
import pickle

from agent import Agent
from game import Game
import numpy as np

class QLearning:
    def __init__(self, game: Game):
        self.game = game
        self.agent = Agent(game)
        self.q_table = self.init_q_table()
        self.learning_rate = 0.1
        self.discount_factor = 0.99
        self.epsilon = 1.0
        self.epsilon_decay = 0.99
        self.min_epsilon = 0.01

    class QLearningAgent:
        def __init__(self, alpha, gamma, epsilon, actions):
            self.alpha = alpha
            self.gamma = gamma
            self.epsilon = epsilon
            self.actions = actions
            self.q_table = self.init_q_table()

        def init_q_table(self):
            # Initialize Q-table with zeros for all state-action pairs
            q_table = {}
            for i in range(1, 494):
                q_table[i] = {}
                for action in self.actions:
                    q_table[i][action] = 0.0
            return q_table

    def choose_action(self, state):
        # Epsilon-greedy policy to choose an action
        if np.random.uniform(0, 1) < self.epsilon:
            # Choose a random action
            action = np.random.choice(self.actions)
        else:
            # Choose the best action based on the Q-table
            state_actions = self.q_table[state]
            max_action_value = max(state_actions.values())
            actions_with_max_value = [action for action, value in state_actions.items() if value == max_action_value]
            action = np.random.choice(actions_with_max_value)
        return action

    def update_q_table(self, state, action, reward, next_state):
        # Update Q-value of the state-action pair using the Q-learning update rule
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state].values())
        new_q = current_q + self.alpha * (reward + self.gamma * next_max_q - current_q)
        self.q_table[state][action] = new_q

    def train(self, num_episodes):
        for i in range(num_episodes):
            state = self.env.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                self.update_q_table(state, action, reward, next_state)
                state = next_state
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

    def save_q_table(self, file_path):
        full_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'AI', 'pokegold-master', file_path)
        with open(full_path, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self, file_path):
        # Your code here
        pass

    def play(self):
        # Your code here
        pass
