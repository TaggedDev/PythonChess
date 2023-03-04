from PythonChess.Code.Figures.Figure import Figure


class Pawn(Figure):
    def implement_move(self, xS, yS, xE, yE):
        self._board.deck[xS][yS] = Pawn(xE, yE, 'p', True, self._board)

    def __str__(self):
        return 'p'

