#!/usr/bin/env python

import atexit
import tetris.tetrislib as t

from tetris.board import Board
from tetris.movement import Movement
from tetris.piece import PIECES, Piece

from pdb import set_trace

original_terminal_state = t.set_terminal_mode()
atexit.register(t.restore_terminal, original_terminal_state)


def main():
    board = Board(10, 10)

    simple_piece = Piece(PIECES[1], (8, 1))
    board = board.add_piece(simple_piece)
    simple_piece = Piece(PIECES[1], (1, 1))
    board = board.add_piece(simple_piece)

    while True:
        print(board)
        direction = t.get_input()

        if not board.piece:
            continue

        bottom, row_i, col_i = board.find_bottom(board.piece)
        if bottom:
            board.piece = None
            continue
        print(bottom, row_i, col_i)

        if direction in {'left', 'right', 'down'}:
            board = Movement.move(board, direction)
        elif direction == 'up':
            board = Movement.rotate(board)

if __name__ == '__main__':
    main()
