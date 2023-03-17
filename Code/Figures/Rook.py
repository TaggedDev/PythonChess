from Code import Board
from Code.Piece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'R'

    def process_move(self, x_end, y_end, color):
        if color != self.color:
            return False

        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что ладья двигается только по вертикали или горизонтали
        if row_start != row_end and col_start != col_end:
            return False

        # Проверяем, что на пути ладьи нет других фигур
        if row_start == row_end:
            # Ладья движется по горизонтали
            for col in range(min(col_start, col_end) + 1, max(col_start, col_end)):
                if Board.board[row_start][col] is not None:
                    return False
        else:
            # Ладья движется по вертикали
            for row in range(min(row_start, row_end) + 1, max(row_start, row_end)):
                if Board.board[row][col_start] is not None:
                    return False

        # Проверка на friendly fire
        end_slot = Board.board[row_end][col_end]
        if end_slot is not None:
            return end_slot.color != self.color

        return True
