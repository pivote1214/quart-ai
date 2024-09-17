import random

from src.game.board import Board
from src.game.piece import Piece
from src.player.player import Player


class Baseline(Player):
    """
    ベースラインのプレイヤー
    - 渡されたコマが勝利手となる場合はその位置に配置
    - それ以外はランダムにプレイ
    """
    def __init__(self, name: str = "Baseline") -> None:
        super().__init__(name)

    def select_piece(self, pieces: list[Piece]) -> Piece:
        """
        ランダムに選択し相手に渡す
        """
        return random.choice(pieces)

    def place_piece(self, board: Board, piece: Piece) -> tuple[int, int]:
        """
        コマを配置する位置を決定
        - 勝利手があればその位置に配置
        - なければランダムに配置
        """
        available = board.available_positions()
        # 勝利手を探す
        for (row, col) in available:
            board.place_piece(row, col, piece)
            if board.check_victory():
                return (row, col)
            else:
                board.grid[row][col] = None

        # 勝利手がなければランダムに配置
        chosen_position = random.choice(available)
        board.place_piece(*chosen_position, piece)
        return chosen_position
