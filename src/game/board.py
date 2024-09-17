from typing import Optional

from src.game.piece import Piece


class Board:
    """
    4x4の盤面を管理
    """
    def __init__(self) -> None:
        # 盤面を4x4のリストで初期化。各セルはNoneまたはPieceインスタンス
        self.grid: list[list[Optional[Piece]]] = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, row: int, col: int, piece: Piece) -> bool:
        """
        指定した位置にコマを配置
        """
        if self.grid[row][col] is None:
            self.grid[row][col] = piece
            return True
        return False

    def is_full(self) -> bool:
        """
        盤面が全て埋まっているかを判定
        """
        for row in self.grid:
            for cell in row:
                if cell is None:
                    return False
        return True

    def check_victory(self) -> bool:
        """
        QUARTが成立しているかを判定
        """
        lines: list[list[Optional[Piece]]] = []

        # 横のライン
        lines.extend(self.grid)

        # 縦のライン
        for col in range(4):
            line = [self.grid[row][col] for row in range(4)]
            lines.append(line)

        # 斜めのライン
        lines.append([self.grid[i][i] for i in range(4)])
        lines.append([self.grid[i][3-i] for i in range(4)])

        for line in lines:
            if None in line:
                continue
            attributes = list(zip(*[piece.attributes() for piece in line]))
            for attr in attributes:
                if all(a == attr[0] for a in attr):
                    return True
        return False

    def available_positions(self) -> list[tuple[int, int]]:
        """
        空いている位置のリストを返します。
        """
        positions: list[tuple[int, int]] = []
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] is None:
                    positions.append((row, col))
        return positions

    def __repr__(self) -> str:
        display = ""
        for row in self.grid:
            display += ' | '.join(
                [str(cell).ljust(20) if cell else 'N/A'.ljust(20) for cell in row]
                ) + "\n"
        return display
