import gym

class Environment:
    def __init__(self, state_size, action_size):
        self.env = gym.make('CartPole-v1')
        self.state_size = state_size
        self.action_size = action_size

    def reset(self):
        state = self.env.reset()
        return state

    def step(self, action):
        next_state, reward, done, info = self.env.step(action)
        if done:
            reward = -10
        else:
            reward = 1
        return next_state, reward, done

    def get_valid_actions(self):
        return range(self.action_size)

    def render(self):
        self.env.render()