from collections import Counter

from src.game.game import Game
from src.game.player import Player
from src.agent.agent import Agent
from src.agent.random_agent import RandomAgent
from src.agent.place1_agent import Place1Agent
from src.agent.select1_agent import Select1Agent
from src.agent.place1_select1_agent import Place1Select1Agent


def simulate_game(
    game: Game, 
    agent1: Agent, 
    agent2: Agent
    ) -> Game:
    while True:
        # check if game is over
        is_gameover, _ = game.is_game_over()
        if is_gameover:
            break
        # play turn
        if game.current_player == Player.Player1:
            agent1.play_turn()
        else:
            agent2.play_turn()
    return game

def get_agent(game: Game, agent_name: str) -> Agent:
    if agent_name == "Random":
        return RandomAgent(game)
    elif agent_name == "Place1":
        return Place1Agent(game)
    elif agent_name == "Select1":
        return Select1Agent(game)
    elif agent_name == "Place1Select1":
        return Place1Select1Agent(game)


if __name__ == "__main__":
    game = Game()
    agent1 = Place1Agent(game)
    agent2 = Select1Agent(game)
    game = simulate_game(game, agent1, agent2)
    game.print_board()
    # agent_names = ["Random", "Place1", "Select1", "Place1Select1"]
    # n_plays = 10 ** 4
    # for i, agent1_name in enumerate(agent_names):
    #     for j, agent2_name in enumerate(agent_names):
    #         if i >= j:
    #             continue
    #         wins = Counter()
    #         for _ in range(n_plays):
    #             game = Game()
    #             agent1 = get_agent(game, agent1_name)
    #             agent2 = get_agent(game, agent2_name)
    #             game = simulate_game(game, agent1, agent2)
    #             _, winner = game.is_game_over()
    #             wins[winner] += 1
    #         print(f"{agent1_name} vs {agent2_name}:")
    #         print(f"{agent1_name} wins: {wins[1]}")
    #         print(f"{agent2_name} wins: {wins[2]}")
    #         print(f"Draws: {wins[0]}")
    #         print("-" * 50)
