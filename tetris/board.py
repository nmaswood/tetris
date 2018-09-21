from piece import Piece
from copy import deepcopy


class Board():
    def __init__(self, width, height, board=None, piece=None):
        self.width = width
        self.height = height

        if board is None:
            self.board = Board.init_board()
        else:
            self.board = board

        if piece is None:
            self.piece = None
        else:
            self.piece = deepcopy(piece)

    def clone(self):
        board = deepcopy(self.board)
        return Board(self.width, self.height, board, self.piece)

    @staticmethod
    def init_board(width, height):
        return [
            [' ' for _ in range(width)]
            for _ in range(height)
        ]

    def remove_old_piece(self):
        copy = self.clone()
        squares = Piece.squares(self.piece)

        for (row_i, col_i) in squares:
            copy.board[row_i][col_i] = ''
        self.piece = None
        return copy

    @staticmethod
    def add_piece(board, piece):
        copy = self.clone()
        squares = Piece.squares(self.piece)

        for (row_i, col_i) in squares:
            copy.board[row_i][col_i] = '#'

        self.piece = piece
        return copy

    def render_board(board, width, height, piece):
        string_builder = []
        stars = ''.join((['*'] * width))

    def update_board():
        pass

    def __str__(self):
        stars = ''.join((['*'] * self.width))

        pass

    def __repr__(self):
        return str(self)
