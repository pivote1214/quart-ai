# COLORS = ['white', 'black']
# HEIGHTS = ['high', 'low']
# SHAPES = ['round', 'square']
# HOLES = ['empty', 'filled']
COLORS  = ['0', '1']
HEIGHTS = ['0', '1']
SHAPES  = ['0', '1']
HOLES   = ['0', '1']

class Piece:
    """
    QUARTのコマを表すクラス
    """
    def __init__(self, color: str, height: str, shape: str, hole: str) -> None:
        self.color = color
        self.height = height
        self.shape = shape
        self.hole = hole

    def attributes(self) -> list[str]:
        return [self.color, self.height, self.shape, self.hole]

    def __repr__(self) -> str:
        
        return f"Piece({self.color}, {self.height}, {self.shape}, {self.hole})"
