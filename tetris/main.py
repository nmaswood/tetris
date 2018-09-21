#!/usr/bin/env python

import atexit
import tetris.tetrislib as t

from tetris.board import Board
from tetris.movement import Movement
from tetris.piece import PIECES, Piece
from threading import Timer

from pdb import set_trace

original_terminal_state = t.set_terminal_mode()
atexit.register(t.restore_terminal, original_terminal_state)


def move_piece_down(board):
    if not board:
        return

    if not board.piece:
        return

    board = Movement.move(board, 'down')


def main():
    state = {}
    board = Board(10, 10)

    init_piece = Piece.random(board.width)
    board = board.add_piece(init_piece)

    timer = Timer(1, move_piece_down, args=(board,))
    timer.start()


    just_replaced_piece = False

    while True:
        print(board)
        direction = t.get_input()
        board = board.line_full_update()

        if not board.piece:
            board.piece = Piece.random(board.width)
            just_replaced_piece = True
            continue

        bottom, row_i, col_i = board.find_bottom(board.piece)
        if bottom:
            if just_replaced_piece:
                print("game over")
                break

            board.piece = None
            continue
        just_replaced_piece = False

        if direction in {'left', 'right', 'down'}:
            board = Movement.move(board, direction)
        elif direction == 'up':
            board = Movement.rotate(board)


if __name__ == '__main__':
    main()
