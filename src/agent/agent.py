from abc import ABC, abstractmethod
from ..game.game import Game

class Agent(ABC):
    def __init__(self, game: Game):
        self.game = game

    @abstractmethod
    def select_position(self):
        pass

    @abstractmethod
    def select_piece(self):
        pass

    def play_turn(self) -> None:
        row, col = self.select_position()
        piece_index = self.select_piece()
        self.game.play_turn(row, col, piece_index)
