from Code import Piece
from Code.Figures.Pawn import Pawn

board = [[None] * 8 for _ in range(8)]


def instantiate_board():
    # Whites
    '''self.board[0][0] = Rook('white', self.board)
    self.board[0][1] = Knight('white', self.board)
    self.board[0][2] = Bishop('white', self.board)
    self.board[0][3] = Queen('white', self.board)
    self.board[0][4] = King('white', self.board)
    self.board[0][5] = Bishop('white', self.board)
    self.board[0][6] = Knight('white', self.board)
    self.board[0][7] = Rook('white', self.board)'''
    for i in range(8):
        board[1][i] = Pawn('white', 1, i)

    # Blacks
    '''self.board[7][0] = Rook('black', self.board)
    self.board[7][1] = Knight('black', self.board)
    self.board[7][2] = Bishop('black', self.board)
    self.board[7][3] = Queen('black', self.board)
    self.board[7][4] = King('black', self.board)
    self.board[7][5] = Bishop('black', self.board)
    self.board[7][6] = Knight('black', self.board)
    self.board[7][7] = Rook('black', self.board)'''
    for i in range(8):
        board[6][i] = Pawn('black', 1, i)

    board[2][2] = Pawn('black', 3, 3)


def algebraic_to_index(algebraic_notation):
    file = ord(algebraic_notation[0]) - ord('a')
    rank = int(algebraic_notation[1]) - 1
    return rank, file


def display_board():
    print('  a b c d e f g h')
    for row in range(8):
        print(row+1, end=' ')
        for col in range(8):
            piece = board[row][col]
            if piece is None:
                print('N', end=" ")
            else:
                print(board[row][col], end=" ")
        print()


def handle_visual_changes(row_start, col_start, row_end, col_end):
    board[col_end][row_end] = board[col_start][row_start]
    board[col_start][row_start] = None
