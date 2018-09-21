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
        if not (0 <= row_i < self.width):
            return True

        if not (0 <= col_i < self.height):
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

        # set_trace()
        squares = piece.squares_no_collisions(self)
        if not squares:
            return None

        for (row_i, col_i) in squares:
            copy.board[row_i][col_i] = '#'

        copy.piece = piece
        return copy

    def update_piece(self, piece):
        removed = self.remove_piece()
        # set_trace()

        added = removed.add_piece(piece)

        if not added:
            raise ValueError("Invalid piece movement")

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

    def find_bottom(self, piece):
        squares = piece.squares()

        for (row_i, col_i) in squares:

            one_past = row_i + 1
            try:
                item_at_square = self.board[one_past][col_i]
            except:
                return (True, row_i, col_i)

            if item_at_square == '#':
                if (one_past, col_i) not in squares:
                    return (True, row_i, col_i)

        return False, None, None

    def _line_full_update(self):

        remove_indexes = set()

        for row_idx, row in enumerate(self.board):
            if all(item == '#' for item in row):
                remove_indexes.add(row_idx)

        new_rows = []
        for row_idx, row in enumerate(self.board):
            if row_idx not in remove_indexes:
                new_rows.append(row)

        while len(new_rows) < self.height:
            new_row = [' ' for _ in range(self.width)]
            new_rows.insert(0, new_row)
        return new_rows

    def line_full_update(self):
        copy = self.clone()
        new_board = self._line_full_update()
        copy.board = new_board
        return copy
