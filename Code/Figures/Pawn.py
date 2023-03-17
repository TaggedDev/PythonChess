from Code import Board
from Code.Piece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color, x, y):
        self.position = x, y
        self.color = color

    def __str__(self):
        return 'p'

    def process_move(self, x_end, y_end):
        row_start, col_start = self.position[0], self.position[1]
        row_end, col_end = x_end, y_end

        # Проверяем, что пешка не атакует свою фигуру
        end_slot = Board.board[row_end][col_end]
        if end_slot is not None:
            if end_slot.color == self.color:
                return False
            # Проверяем, что пешка атакует фигуру противника только по диагонали
            else:
                if self.color == 'white':
                    return row_end - row_start == 1 and abs(col_end - col_start) == 1
                else:
                    return row_start - row_end == 1 and abs(col_end - col_start) == 1


        # Проверка движения пешки строго по вертикали на <= 2 по y
        if col_end != col_start or abs(col_end - col_start) > 2:
            return False

        # Проверка движения на 2 строго при стартовой позиции
        if self.color == 'white':
            delta = row_end - row_start
            if row_start != 1 and delta == 2:
                return False
        else:
            delta = row_start - row_end
            if row_start != 6 and delta == 2:
                return False


        # Проверка на перепрыгивание фигуры при delta == 2
        if abs(row_start - row_end) == 2:
            if self.color == 'white':
                if Board.board[row_start + 1][col_start] is not None:
                    return False
            else:
                if Board.board[row_start - 1][col_start] is not None:
                    return False

        # Если все проверки пройдены, то ход совершается успешно
        return True
