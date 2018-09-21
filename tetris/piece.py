from copy import deepcopy

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

    def clone(self):
        copy = deepcopy(self.piece_type)
        return Piece(copy, self.center)

    @staticmethod
    def rotate(piece):
        pass

    @staticmethod
    def collision(board, piece):
        pass

    @staticmethod
    def squares(piece):
        center, piece_type = piece.center, piece.piece_type

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
