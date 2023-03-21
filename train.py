import random
from agent import Agent
from environment import Environment

# create environment and agent
env = Environment(state_size=4, action_size=2)
agent = Agent(state_size=4, action_size=2)

# train the agent
for episode in range(1000):
    state = env.reset()
    done = False
    while not done:
        # get action from agent
        action = agent.get_action(state, env.get_valid_actions())

        # take action in environment
        next_state, reward, done = env.step(action)

        # update agent's Q-table
        agent.update_q_table(state, action, next_state, reward)

        # update state
        state = next_state

    # decay agent's epsilon value after each episode
    agent.decay_epsilon()

# save the trained Q-table
agent.save_q_table() 