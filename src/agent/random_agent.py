import random
from ..game.game import Game

class RandomAgent:
    def __init__(self, game: Game):
        self.game = game

    def select_position(self):
        available_positions = [(r, c) for r in range(4) for c in range(4) if self.game.board.grid[r][c] is None]
        return random.choice(available_positions)

    def select_piece(self):
        return random.randrange(len(self.game.available_pieces))

    def play_turn(self):
        # Select a random position to place the current piece
        row, col = self.select_position()
        # Select a random piece for the opponent
        piece_index = self.select_piece()
        self.game.play_turn(row, col, piece_index)
