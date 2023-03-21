import random


class Environment:
    def __init__(self):
        self.grid_size = 10
        self.goal_pos = (self.grid_size - 1, self.grid_size - 1)
        self.agent_pos = (0, 0)

    def reset(self):
        self.agent_pos = (0, 0)

    def step(self, action):
        if action == 'up':
            self.agent_pos = (max(0, self.agent_pos[0] - 1), self.agent_pos[1])
        elif action == 'down':
            self.agent_pos = (min(self.grid_size - 1, self.agent_pos[0] + 1), self.agent_pos[1])
        elif action == 'left':
            self.agent_pos = (self.agent_pos[0], max(0, self.agent_pos[1] - 1))
        elif action == 'right':
            self.agent_pos = (self.agent_pos[0], min(self.grid_size - 1, self.agent_pos[1] + 1))
        done = (self.agent_pos == self.goal_pos)
        reward = 1 if done else -0.1
        return self.agent_pos, reward, done

    def get_valid_actions(self):
        valid_actions = []
        if self.agent_pos[0] > 0:
            valid_actions.append('up')
        if self.agent_pos[0] < self.grid_size - 1:
            valid_actions.append('down')
        if self.agent_pos[1] > 0:
            valid_actions.append('left')
        if self.agent_pos[1] < self.grid_size - 1:
            valid_actions.append('right')
        return valid_actions

    def render(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) == self.agent_pos:
                    print('A', end=' ')
                elif (i, j) == self.goal_pos:
                    print('G', end=' ')
                else:
                    print('-', end=' ')
            print()
        print()