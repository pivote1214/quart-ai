# game/board.py

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, row, col, piece):
        if self.grid[row][col] is not None:
            raise ValueError(f"cell ({row}, {col}) is already occupied")
        self.grid[row][col] = piece

    def check_victory(self):
        lines = []

        # 水平と垂直のラインを収集
        for i in range(4):
            lines.append([self.grid[i][j] for j in range(4)])  # 行
            lines.append([self.grid[j][i] for j in range(4)])  # 列

        # 斜めのラインを収集
        lines.append([self.grid[i][i] for i in range(4)])          # 左上から右下
        lines.append([self.grid[i][3 - i] for i in range(4)])      # 右上から左下

        # 各ラインで共通属性をチェック
        for line in lines:
            if None in line:
                continue
            for attr_index in range(4):
                attr_values = [piece.get_attributes()[attr_index] for piece in line]
                if all(value == attr_values[0] for value in attr_values):
                    return True  # 勝利条件を満たす
        return False

    def is_full(self):
        return all(self.grid[row][col] is not None for row in range(4) for col in range(4))

    def get_empty_positions(self):
        positions = [(row, col) for row in range(4) for col in range(4) if self.grid[row][col] is None]
        return positions

    def __repr__(self):
        board_str = ''
        for row in self.grid:
            row_str = ' | '.join([' ' * 11 if piece is None else str(piece) for piece in row])
            board_str += row_str + '\n'
        return board_str
