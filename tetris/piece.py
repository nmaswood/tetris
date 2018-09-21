from copy import deepcopy
import numpy as np
from random import choice, randint

from pdb import set_trace


PIECES = [
    (
        [1, 1, 1, 1],
    ),
    (
        [1, 0, 0],
        [1, 1, 1]
    ),
    (
        [0, 0, 1],
        [1, 1, 1]
    ),
    (
        [1, 1],
        [1, 1]
    ),
    (
        [0, 1, 1],
        [1, 1, 0]
    ),
    (
        [1, 1, 1],
        [0, 1, 0]
    ),
    (
        [1, 1, 0],
        [0, 1, 1]
    ),
]


class Piece:

    def __init__(self, piece_type, center):
        self.piece_type = deepcopy(piece_type)
        self.center = center

    def __str__(self):
        return '\n'.join(['\n'.join(map(str, self.piece_type)), str(self.center)])

    def __repr__(self):
        return str(self)

    def clone(self):
        copy = deepcopy(self.piece_type)
        return Piece(copy, self.center)

    def move(self, direction):
        copy = self.clone()
        (row, col) = copy.center

        if direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        elif direction == 'left':
            col -= 1

        copy.center = (row, col)

        return copy

    def rotate(self):
        copy = self.clone()
        rotated = list(zip(*copy.piece_type[::-1]))
        copy.piece_type = rotated
        return copy

    def squares(self):
        center, piece_type = self.center, self.piece_type

        coordinates = set()

        row_0, col_0 = center

        for row_idx, row in enumerate(piece_type):
            for col_idx, col in enumerate(row):
                if col == 0:
                    continue
                row_prime = row_idx + row_0
                col_prime = col_idx + col_0
                coordinates.add((row_prime, col_prime))
        return coordinates

    def squares_no_collisions(self, board):
        coordinates = self.squares()

        for (row_i, col_i) in coordinates:
            if board.invalid(row_i, col_i):
                return None
        return coordinates

    @staticmethod
    def random():
        piece = Piece(choice(PIECES), (0,0))

        for _ in range(randint(1, 5)):
            piece = piece.rotate()
        return piece
