class Piece:
    def __init__(
        self,
        color: int, 
        shape: int, 
        height: int, 
        surface: int
        ):
        self.color = color  # 0 for Black, 1 for White
        self.shape = shape  # 0 for Round, 1 for Square
        self.height = height  # 0 for Tall, 1 for Short
        self.surface = surface  # 0 for Hollow, 1 for Solid
