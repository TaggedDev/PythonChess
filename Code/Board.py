import Piece
from Figures.Bishop import Bishop
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Rook import Rook

board = [[None] * 8 for _ in range(8)]


def instantiate_board():
    # Whites
    board[0][0] = Rook('white', 0, 0)
    board[0][1] = Knight('white', 0, 1)
    board[0][2] = Bishop('white', 0, 2)
    board[0][3] = Queen('white', 0, 3)
    board[0][4] = King('white', 0, 4)
    board[0][5] = Bishop('white', 0, 5)
    board[0][6] = Knight('white', 0, 6)
    board[0][7] = Rook('white', 0, 7)
    for i in range(8):
        board[1][i] = Pawn('white', 1, i)

    # Blacks
    board[7][0] = Rook('black', 7, 0)
    board[7][1] = Knight('black', 7, 1)
    #board[7][2] = Bishop('black', 7, 2)
    #board[7][3] = Queen('black', 7, 3)
    board[7][4] = King('black', 7, 4)
    #board[7][5] = Bishop('black', 7, 2)
    #board[7][6] = Knight('black', 7, 6)
    board[7][7] = Rook('black', 7, 7)
    for i in range(8):
        board[6][i] = Pawn('black', 6, i)


def algebraic_to_index(algebraic_notation):
    file = ord(algebraic_notation[0]) - ord('a')
    rank = int(algebraic_notation[1]) - 1
    return rank, file


def display_board():
    print('  aa bb cc dd ee ff gg hh')
    for row in range(8):
        print(row + 1, end=' ')
        for col in range(8):
            piece = board[row][col]
            if piece is None:
                print('__', end=" ")
            else:
                print(board[row][col], end=" ")
        print()


def handle_visual_changes(row_start, col_start, row_end, col_end):
    board[col_end][row_end] = board[col_start][row_start]
    board[col_end][row_end].update_position(row_end, col_end)
    board[col_start][row_start] = None

def is_slot_attacked(col, row):
    for row in range(8):
        for col in range(8):
            slot = board[row][col]
            if slot is not None:
                if slot.process_move(col , row):
                    return True
    return False

def handle_visual_changes_castling(is_white: bool, type: str) -> None:
    if type == 'short':
        if is_white:
            board[0][5] = board[0][7]
            board[0][6] = board[0][4]
            board[0][4] = None
            board[0][7] = None
        else:
            board[7][5] = board[7][7]
            board[7][6] = board[7][4]
            board[7][4] = None
            board[7][7] = None
    else:
        if is_white:
            board[0][2] = board[0][0]
            board[0][3] = board[0][4]
            board[0][4] = None
            board[0][0] = None
        else:
            board[7][2] = board[7][0]
            board[7][3] = board[7][4]
            board[7][4] = None
            board[7][0] = None
