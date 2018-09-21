class Movement:

    def __init__(self):
        pass

    @staticmethod
    def side_ways(board, movement):
        piece_prime = board.piece.move(movement)
        try:
            new_board = board.update_piece(piece_prime)
        except ValueError:
            return board

        return new_board
