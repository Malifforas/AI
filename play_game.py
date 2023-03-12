import gym

# Import the ROM and emulator
env = gym.make('gym_emu:emu-v0', game_path='C:/Users/Blizzard/Desktop/AI/Pokemon - HeartGold Version (USA).nds')

# Get the initial state
state = env.reset()

# Loop until the game is done
done = False
while not done:
    # Take an action
    action = env.action_space.sample()
    next_state, reward, done, info = env.step(action)

    # Print some information about the step
    print("Action:", action)
    print("Reward:", reward)
    print("Done:", done)
    print("Info:", info)