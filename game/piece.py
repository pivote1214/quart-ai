# game/piece.py

class Piece:
    def __init__(
        self, 
        color: int, 
        height: int, 
        shape: int, 
        hole: int
        ):
        self.color = color      # 0: white,     1: black
        self.height = height    # 0: low,       1: high
        self.shape = shape      # 0: circle,    1: square
        self.hole = hole        # 0: no hole,   1: hole

    def get_attributes(self):
        return [self.color, self.height, self.shape, self.hole]

    def __repr__(self):
        attrs = ''.join(map(str, self.get_attributes()))
        return f"Piece({attrs})"


if __name__ == '__main__':
    piece = Piece(0, 1, 0, 1)
    print(piece)
