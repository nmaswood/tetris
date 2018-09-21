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
    simple_piece = Piece(PIECES[0], (0, 0))
    board = board.add_piece(simple_piece)

    while True:
        print(board)
        direction = t.get_input()

        # rename func at some point
        if direction in {'left', 'right', 'down'}:
            board = Movement.side_ways(board, direction)

if __name__ == '__main__':
    main()
