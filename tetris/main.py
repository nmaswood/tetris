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
        direction = t.get_input()

        if direction in {'left', 'right'}:
            modified_board = Movement.side_ways(board, direction)
            if modified_board:
                board = modified_board


if __name__ == '__main__':
    main()
