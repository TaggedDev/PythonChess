import Board
from Piece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return f'{self.color[0]}B'

    def process_move(self, x_end, y_end, color=None):

        if color is None:
            if self.color == 'white':
                color = 'black'
            else:
                color = 'white'

        if color != self.color:
            return False
        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что слон двигается по диагонали
        if abs(row_start - row_end) != abs(col_start - col_end):
            return False

        # Проверяем, что на пути движения слона нет других фигур
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

        # Если все проверки прошли успешно, то перемещаем слона на новую позицию
        return True