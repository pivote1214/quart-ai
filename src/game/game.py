import random

from .board import Board
from .piece import Piece
from .player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.available_pieces = self.create_pieces()
        self.selected_piece = self.available_pieces.pop(random.randrange(len(self.available_pieces)))
        self.current_player = Player.Player1

    def create_pieces(self) -> list[Piece]:
        pieces = []
        for color in range(2):  # 0 (Black), 1 (White)
            for shape in range(2):  # 0 (Round), 1 (Square)
                for height in range(2):  # 0 (Tall), 1 (Short)
                    for surface in range(2):  # 0 (Hollow), 1 (Solid)
                        pieces.append(Piece(color, shape, height, surface))
        return pieces

    def play_turn(self, row, col, piece_index=None):
        self.board.place_piece(row, col, self.selected_piece)
        if piece_index is not None:
            self.selected_piece = self.available_pieces.pop(piece_index)
        self.current_player = Player.Player2 if self.current_player == Player.Player1 else Player.Player1

    def is_game_over(self) -> tuple[bool, int | None]:
        if self.board.check_winner():
            return True, 1 if self.current_player == Player.Player2 else 2
        elif len(self.available_pieces) == 0:
            return True, 0
        else:
            return False, None

    def print_board(self) -> None:
        for row in self.board.grid:
            for cell in row:
                if cell is None:
                    print("None", end=" " * 6)
                else:
                    piece_str = f"{cell.color}-{cell.shape}-{cell.height}-{cell.surface}"
                    print(piece_str, end=" " * (10 - len(piece_str)))
            print()
