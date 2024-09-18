# game/game_state.py

from .board import Board
from .constants import ALL_PIECES

class GameState:
    def __init__(self):
        self.board = Board()
        self.available_pieces = ALL_PIECES.copy()
        self.next_piece = None
        self.turn = 0  # 0: プレイヤー1, 1: プレイヤー2

    def set_next_piece(self, piece):
        if piece not in self.available_pieces:
            raise ValueError("Cannot set a piece that is not available.")
        self.next_piece = piece
        self.available_pieces.remove(piece)

    def place_next_piece(self, x, y):
        if self.next_piece is None:
            raise ValueError("Next piece is not set.")
        self.board.place_piece(x, y, self.next_piece)
        self.next_piece = None
        self.turn = (self.turn + 1) % 2  # 手番を交代

    def is_game_over(self):
        return self.board.check_victory() or self.board.is_full()

    def get_winner(self):
        if self.board.check_victory():
            return (self.turn + 1) % 2  # 勝者のプレイヤー番号
        return None  # 引き分けまたはゲーム続行中

    def __repr__(self):
        return f"Turn: Player {self.turn + 1}\n{self.board}"
