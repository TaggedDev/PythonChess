from Desk.Slot import Slot


class Board:
    def __init__(self):
        self.deck = self.generate_deck()

    @staticmethod
    def generate_deck():
        """
        Generates basic deck with figures and empty slots
        :return: A default deck configuration
        """
        desk = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                row.append(Slot(x, y))
            desk.append(row)

        desk[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        desk[1] = ['p'] * 8
        desk[6] = ['p'] * 8
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

