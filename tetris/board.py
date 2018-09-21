from tetris.piece import Piece
from copy import deepcopy
from pdb import set_trace


class Board():
    def __init__(self, width, height, board=None, piece=None):
        self.width = width
        self.height = height

        if board is None:
            self.board = Board.init_board(width, height)
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

    def invalid(self, row_i, col_i):
        if 0 < row_i <= self.board.width:
            return True

        if 0 < col_i <= self.board.height:
            return True

        if self.board[row_i][col_i] != ' ':
            return True

        return False

    def remove_piece(self):
        copy = self.clone()

        if not self.piece:
            return copy

        squares = Piece.squares(copy.piece)

        for (row_i, col_i) in squares:
            copy.board[row_i][col_i] = ' '
        copy.piece = None
        return copy

    def add_piece(self, piece):
        copy = self.clone()
        copy.piece = piece

        squares = Piece.squares(piece)

        for (row_i, col_i) in squares:
            copy.board[row_i][col_i] = '#'

        copy.piece = piece
        return copy

    def update_piece(self, piece):
        removed = self.remove_piece()
        added = removed.add_piece(piece)

        return added

    def __str__(self):
        string_builder = []
        stars = ''.join((['*'] * (self.width + 2)))
        string_builder.append(stars)
        for row in self.board:
            addition = ''.join([
                '|',
                ''.join(row),
                '|'
            ])
            string_builder.append(addition)
        string_builder.append(stars)

        return '\n'.join(string_builder)

    def __repr__(self):
        return str(self)
