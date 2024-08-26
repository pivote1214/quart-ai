import random

from board import Board
from game.piece import Piece
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.available_pieces = self.create_pieces()
        self.selected_piece = self.available_pieces.pop(random.randrange(len(self.available_pieces)))
        self.current_player = Player.Player1

    def create_pieces(self):
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

    def is_game_over(self):
        return self.board.check_winner()
