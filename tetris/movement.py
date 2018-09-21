class Movement:

    def __init__(self):
        pass

    @staticmethod
    def side_ways(board, movement):
        piece_prime = board.piece.move(movement)

        if board.invalid(piece_prime):
            return

        new_board = board.update_piece(piece_prime)
        return new_board

