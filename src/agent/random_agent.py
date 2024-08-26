import random
from .agent import Agent


class RandomAgent(Agent):
    def select_position(self):
        available_positions = [(r, c) for r in range(4) for c in range(4) if self.game.board.grid[r][c] is None]
        return random.choice(available_positions)

    def select_piece(self):
        return random.randrange(len(self.game.available_pieces))
