#!/usr/bin/env python

import atexit
import tetris.tetrislib as t
from tetris.board import Board

original_terminal_state = t.set_terminal_mode()
atexit.register(t.restore_terminal, original_terminal_state)


def main():
    init_board = Board(10, 10)
    print(init_board)
    while True:
        direction = t.get_input()

        print(direction)


if __name__ == '__main__':
    main()
