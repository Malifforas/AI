from game import Game
from q_learning import QLearning

def main():
    rom_path = "C:/Users/Blizzard/Desktop/AI/Pokemon - HeartGold Version (USA).nds"
    game = Game(rom_path)
    q_learning = QLearning(game)
    q_learning.train()
    q_learning.save_q_table('q_table.pkl')
    q_learning.play()

if __name__ == '__main__':
    main()