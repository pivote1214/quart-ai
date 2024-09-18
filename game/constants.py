# game/constants.py

from game.piece import Piece

ALL_PIECES = []

for color in range(2):
    for height in range(2):
        for shape in range(2):
            for hole in range(2):
                piece = Piece(color, height, shape, hole)
                ALL_PIECES.append(piece)
