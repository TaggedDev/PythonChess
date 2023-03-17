from Code import Board
from Code.Piece import ChessPiece


class King(ChessPiece):
    def __init__(self, color, x, y):
        self.position = x, y
        self.color = color

    def __str__(self):
        return 'K'

    def process_move(self, x_end, y_end):
        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что король двигается не более чем на одну клетку в любом направлении
        if abs(row_start - row_end) > 1 or abs(col_start - col_end) > 1:
            return False

        # Проверяем, что на конечной позиции нет фигуры того же цвета
        if Board.board[row_end][col_end] is not None and Board.board[row_end][col_end].color == self.color:
            return False

        # Если все проверки прошли успешно, то перемещаем короля на новую позицию
        return True