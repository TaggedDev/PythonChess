from Code import Board
from Code.Piece import ChessPiece


class Queen(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return f'{self.color[0]}Q'

    def process_move(self, x_end, y_end, color):
        if color != self.color:
            return False

        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что королева двигается по диагонали или прямой линии
        if abs(row_start - row_end) != abs(col_start - col_end) and row_start != row_end and col_start != col_end:
            return False

        # Проверяем, что на пути движения королевы нет других фигур
        if row_start == row_end:
            col_step = 1 if col_end > col_start else -1
            curr_col = col_start + col_step
            while curr_col != col_end:
                if Board.board[row_start][curr_col] is not None:
                    return False
                curr_col += col_step
        elif col_start == col_end:
            row_step = 1 if row_end > row_start else -1
            curr_row = row_start + row_step
            while curr_row != row_end:
                if Board.board[curr_row][col_start] is not None:
                    return False
                curr_row += row_step
        else:
            row_step = 1 if row_end > row_start else -1
            col_step = 1 if col_end > col_start else -1
            curr_row, curr_col = row_start + row_step, col_start + col_step
            while curr_row != row_end and curr_col != col_end:
                if Board.board[curr_row][curr_col] is not None:
                    return False
                curr_row += row_step
                curr_col += col_step

        # Проверяем, что на конечной позиции нет фигуры того же цвета
        if Board.board[row_end][col_end] is not None and Board.board[row_end][col_end].color == self.color:
            return False

        # Если все проверки прошли успешно, то перемещаем королеву на новую позицию
        return True
