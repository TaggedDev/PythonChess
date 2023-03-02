from Desk.Slot import Slot
from Figures.Pawn import Pawn


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
                    row.append(Pawn(x, y, 'p', False, self))
                elif x == 6:
                    row.append(Pawn(x, y, 'p', True, self))
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

    def move_pawn(self):
        self.deck[1][1].move_towards('f1', 'f5')

