import os
import sys
from subprocess import Popen, PIPE

# The board is represented as an array of arrays, with 10 rows and 10 columns.
board_size = { "x": 10, "y": 10 }
board = []

# Setup the board.
for i in range(0, board_size["y"]):
    board.append([0 for i in range(0, board_size["x"])])

# Draws the contents of the board with a border around it.
def draw_board():
    board_border = "".join(["*" for i in range(0, board_size["x"] + 2)])
    print(board_border)
    for y in range(0, board_size["y"]):
        line = "|"
        for x in range(0, board_size["x"]):
            line += ("#" if board[y][x] == 1 else " ")
        line += "|"
        print(line)
    print(board_border)

# Waits for a single character of input and returns the string "left", "down", "right", "up", or None.
def get_input():
    original_terminal_state = None

    input = sys.stdin.read(1)

    # The arrow keys are read from stdin as an escaped sequence of 3 bytes.
    escape_sequence = "\x1b"
    ctrl_c = "\003"
    if input == escape_sequence:
        # The next two bytes will indicate which arrow keyw as pressed.
        character = sys.stdin.read(2)
        arrow_character_codes = dict(D="left", B="down", C="right", A="up")
        return arrow_character_codes.get(character[1], None)
    elif input == ctrl_c:
        sys.exit()

    return None

def set_terminal_mode():
    original_terminal_state = Popen(b"stty -g", stdout=PIPE, shell=True).communicate()[0]
    os.system(b"stty -icanon -echo -isig")
    return original_terminal_state

def restore_terminal(state):
    os.system(b"stty " + state)
