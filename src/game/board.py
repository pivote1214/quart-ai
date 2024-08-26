from typing import Optional

from .piece import Piece

class Board:
    def __init__(self):
        self.grid: list[list[Piece]] = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, row: int, col: int, piece: Piece) -> None:
        if self.grid[row][col] is not None:
            raise ValueError("The cell is already occupied")
        self.grid[row][col] = piece

    def check_winner(self) -> bool:
        return any([
            self.check_rows(),
            self.check_columns(),
            self.check_diagonals()
        ])

    def check_rows(self) -> bool:
        return any(self.check_line(*row) for row in self.grid)

    def check_columns(self) -> bool:
        return any(self.check_line(*[self.grid[r][col] for r in range(4)]) for col in range(4))

    def check_diagonals(self) -> bool:
        return (
            self.check_line(self.grid[0][0], self.grid[1][1], self.grid[2][2], self.grid[3][3]) or
            self.check_line(self.grid[0][3], self.grid[1][2], self.grid[2][1], self.grid[3][0])
        )

    def check_line(
        self, 
        a: Optional[Piece], 
        b: Optional[Piece], 
        c: Optional[Piece], 
        d: Optional[Piece]
        ) -> bool:
        if None in [a, b, c, d]:
            return False
        all_same_color = a.color == b.color == c.color == d.color
        all_same_shape = a.shape == b.shape == c.shape == d.shape
        all_same_height = a.height == b.height == c.height == d.height
        all_same_surface = a.surface == b.surface == c.surface == d.surface

        return any([all_same_color, all_same_shape, all_same_height, all_same_surface])
