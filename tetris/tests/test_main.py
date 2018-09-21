from tetris.piece import PIECES, Piece
from tetris.board import Board
from tetris.movement import Movement

from pdb import set_trace


def test_squares():
    center = (0, 0)
    long_piece = PIECES[0]

    piece = Piece(long_piece, center)
    res = Piece.squares(piece)

    assert res == {(0, 1), (0, 3), (0, 0), (0, 2)}

    center = (2, 2)
    L = PIECES[2]
    piece = Piece(L, center)

    res = Piece.squares(piece)

    assert res == {(3, 2), (3, 4), (2, 4), (3, 3)}


def test_board_str():

    board = Board(10, 10)
    assert str(board) == '************\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n************'  # noqa

    center = (2, 2)
    L = PIECES[2]
    piece = Piece(L, center)

    board_with_l = board.add_piece(piece)

    assert str(board_with_l) == '************\n|          |\n|          |\n|    #     |\n|  ###     |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n************'  # noqa

    empty_board = board_with_l.remove_piece()

    assert str(empty_board) == '************\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n************'  # noqa


def test_move():
    board = Board(10, 10)
    simple_piece = Piece(PIECES[0], (0, 0))
    board = board.add_piece(simple_piece)

    right_one = Movement.move(board, 'right')
    assert str(right_one) == '************\n| ####     |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n|          |\n************'  # noqa

    left_one = Movement.move(board, 'left')
    assert str(left_one) == str(board)

