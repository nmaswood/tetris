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

    def __init__(self, piece_type, x_offset, y_offset):
        self.piece_type = piece_type
        self.x_offset = x_offset
        self.y_offset = y_offset

    @staticmethod
    def rotate(piece):
        pass

    @staticmethod
    def collision(board, piece):
        pass

