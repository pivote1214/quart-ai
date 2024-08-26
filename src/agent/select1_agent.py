import random
from .agent import Agent


class Select1Agent(Agent):
    def select_position(self):
        available_positions = [(r, c) for r in range(4) for c in range(4) if self.game.board.grid[r][c] is None]
        return random.choice(available_positions)

    def select_piece(self):
        # Avoid giving a piece that would allow the opponent to win
        for index, piece in enumerate(self.game.available_pieces):
            will_cause_win = False
            for r in range(4):
                for c in range(4):
                    if self.game.board.grid[r][c] is None:
                        # Temporarily place the piece
                        self.game.board.grid[r][c] = piece
                        if self.game.board.check_winner():
                            will_cause_win = True
                        # Revert the board to its original state
                        self.game.board.grid[r][c] = None
                        if will_cause_win:
                            break
                if will_cause_win:
                    break
            if not will_cause_win:
                return index
        # If all pieces would cause a win, just return a random piece
        return random.randrange(len(self.game.available_pieces))
