#!/usr/bin/env python

import atexit
from tetrislib import *

original_terminal_state = set_terminal_mode()
atexit.register(restore_terminal, original_terminal_state)

# This example code draws a horizontal bar 4 squares long.
row = 2
board[row][5] = 1
board[row][6] = 1
board[row][7] = 1
board[row][8] = 1

draw_board()

# This code waits for input until the user hits a keystroke. getinput() returns one of "left", "up", "right",
# "down".
while True:
    get_input()
