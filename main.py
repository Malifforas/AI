from q_learning import QLearningAgent
from emulator_interaction import EmulatorInteraction

def main():
    # Create emulator interaction object
    emu_int = EmulatorInteraction()

    # Create Q-learning agent object
    actions = ['LEFT', 'RIGHT', 'UP', 'DOWN', 'A', 'B', 'SELECT', 'START']
    q_agent = QLearningAgent(actions)

    # Start the emulator
    emu_int.start_emulator()

    # Play the game with the Q-learning agent
    while True:
        state = emu_int.get_state()
        action = q_agent.get_action(state)
        emu_int.take_action(action)

if __name__ == '__main__':
    main()