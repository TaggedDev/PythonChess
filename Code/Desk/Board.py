from PythonChess.Code.Desk.Slot import Slot
from PythonChess.Code.Figures.Figure import Figure
from PythonChess.Code.Figures.Pawn import Pawn


class Board:
    def __init__(self):
        self.deck = self.generate_deck()

    def generate_deck(self):
        """
        Generates basic deck with figures and empty slots
        :return: A default deck configuration
        """
        desk = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                if x == 1:
                    pawn = Pawn(x, y, 'p', False, self)
                    row.append(Slot(x, y, pawn))
                elif x == 6:
                    pawn = Pawn(x, y, 'p', True, self)
                    row.append(Slot(x, y, pawn))
                else:
                    row.append(Slot(x, y))
            desk.append(row)

        desk[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        desk[7] = ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        return desk

    def display_deck(self):
        """
        Prints 2d array (deck)
        :return: None
        """
        for row in self.deck:
            for each in row:
                print(each, end=' ')
            print()

    def handle_player_turn(self, turn):
        x1, y1 = Figure.translate_algebric_notation(turn[:2])
        x2, y2 = Figure.translate_algebric_notation(turn[2:])
        self.deck[x1][y1].figure.move_towards(x2, y2)
