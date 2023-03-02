from Figures.Figure import Figure


class Pawn(Figure):
    def implement_move(self, xS, yS, xE, yE):
        self._board.deck[5][4] = Pawn(5, 4, 'p', True, self._board)

