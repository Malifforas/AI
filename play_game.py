import gym
import numpy as np

# Load the emulator
env = gym.make('gym_emu:emu-v0', game_path='C:/Users/Blizzard/Desktop/AI/Pokemon - HeartGold Version (USA).nds',
               emulator_path='C:/Users/Blizzard/Desktop/AI/DeSmuME_0.9.13_x64.exe')

# Get the initial state
state = env.reset()

# Main game loop
while True:
    # Sample a random action
    action = env.action_space.sample()

    # Take a step in the environment
    next_state, reward, done, info = env.step(action)

    # Check if the game has ended
    if done:
        break

env.close()