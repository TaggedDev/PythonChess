from Code import Board
from Code.Piece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return f'{self.color[0]}p'

    def process_move(self, x_end, y_end, color):
        if color != self.color:
            return False

        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что пешка двигается только вперед
        if self.color == 'white':
            if row_end <= row_start:
                return False
        else:
            if row_end >= row_start:
                return False

        # Проверяем, что пешка двигается на одну или две клетки вперед при первом ходе
        if col_start == col_end:
            if self.color == 'white':
                if row_start == 1 and row_end == 3:
                    if Board.board[2][col_start] is not None:
                        return False
                elif row_end - row_start == 1:
                    if Board.board[row_end][col_end] is not None:
                        return False
                elif row_end - row_start != 1:
                    return False
            else:
                if row_start == 6 and row_end == 4:
                    if Board.board[5][col_start] is not None:
                        return False
                elif row_start - row_end == 1:
                    if Board.board[row_end][col_end] is not None:
                        return False
                elif row_end - row_start != 1:
                    return False
        else:
            # Проверяем, что пешка двигается по диагонали только для захвата фигуры противника
            if abs(col_start - col_end) != 1 or abs(row_start - row_end) != 1:
                return False

            # Проверяем, что на конечной позиции находится фигура противника
            if Board.board[row_end][col_end] is None or Board.board[row_end][col_end].color == self.color:
                return False

        # Если все проверки прошли успешно, то перемещаем пешку на новую позицию
        return True
