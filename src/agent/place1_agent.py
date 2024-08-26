import random
from ..game.game import Game

class Place1Agent:
    def __init__(self, game: Game):
        self.game = game

    def select_position(self):
        # Check if there is a winning position
        for r in range(4):
            for c in range(4):
                if self.game.board.grid[r][c] is None:
                    # Temporarily place the current piece
                    self.game.board.grid[r][c] = self.game.selected_piece
                    if self.game.board.check_winner():
                        # Revert the board to its original state
                        self.game.board.grid[r][c] = None
                        return r, c
                    # Revert the board to its original state
                    self.game.board.grid[r][c] = None
        
        # If no winning position, choose randomly
        available_positions = [(r, c) for r in range(4) for c in range(4) if self.game.board.grid[r][c] is None]
        return random.choice(available_positions)

    def select_piece(self):
        return random.randrange(len(self.game.available_pieces))

    def play_turn(self):
        # Select the best position to place the current piece
        row, col = self.select_position()
        # Select a random piece for the opponent
        piece_index = self.select_piece()
        self.game.play_turn(row, col, piece_index)
