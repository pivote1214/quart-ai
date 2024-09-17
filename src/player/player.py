from typing import List, Tuple

from src.game.board import Board
from src.game.piece import Piece


class Player:
    """
    プレイヤーの基底クラス
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def select_piece(self, pieces: List[Piece]) -> Piece:
        """
        相手に渡すコマを選択
        """
        raise NotImplementedError

    def place_piece(self, board: Board, piece: Piece) -> Tuple[int, int]:
        """
        渡されたコマを盤面に配置
        """
        raise NotImplementedError
