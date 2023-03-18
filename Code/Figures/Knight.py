from Code import Board
from Code.Piece import ChessPiece


class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return f'{self.color[0]}H'

    def process_move(self, x_end, y_end, color):
        if color != self.color:
            return False

        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что конь двигается на L-образной траектории
        delta_row = abs(row_start - row_end)
        delta_col = abs(col_start - col_end)
        if not((delta_row == 2 and delta_col == 1) or (delta_row == 1 and delta_col == 2)):
            return False

        # Проверяем, что на конечной позиции нет фигуры того же цвета
        slot_end = Board.board[row_end][col_end]
        if slot_end is not None:
            if Board.board[row_end][col_end].color == self.color:
                return False

        # Если все проверки прошли успешно, то перемещаем коня на новую позицию
        return True
