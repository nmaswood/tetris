class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._board = Board.init_board()

        self.piece = None
        self.piece_location = None

    @staticmethod
    def init_board(width, height):
        return [
            [' ' for _ in range(width)]
            for _ in range(height)
        ]

    @staticmethod
    def render_board(board, width, height, piece):
        pass

    def __str__(self):
        stars = ''.join((['*'] * self.width))
        bor

        pass

    def __repr__(self):
        return str(self)

