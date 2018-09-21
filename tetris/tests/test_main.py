from tetris.piece import PIECES, Piece
from pdb import set_trace


def test_squares():
    center = (0, 0)
    long_piece = PIECES[0]

    res = Piece.squares(center, long_piece)
    assert res == {(0, 1), (0, 3), (0, 0), (0, 2)}

    center = (2, 2)
    L = PIECES[2]

    res = Piece.squares(center, L)

    assert res == {(3, 2), (3, 4), (2, 4), (3, 3)}
