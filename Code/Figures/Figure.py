from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x, y, icon, is_white, board):
        self.x = x
        self.y = y
        self._is_white = is_white
        self._position = [x, y]
        self._icon = icon
        self._board = board

    @static

    def move_towards(self, x2, y2):
        self.implement_move(self.x, self.y, x2, y2)

    @staticmethod
    def translate_algebric_notation(string):
        try:
            x = 8 - int(string[1])
            y = ord(string[0]) - 97
            return x, y
        except ValueError as e:
            raise ValueError('Invalid notation values')

    @abstractmethod
    def implement_move(self, xS, yS, xE, yE):
        pass

    @property
    def board(self):
        return self._board

    @property
    def is_white(self):
        return self._is_white

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if any([0 > i or i < 7 for i in value]):
            raise ValueError("Value must be between 0 and 7")
        self._position = value

    @property
    def icon(self):
        return self._icon

    def __str__(self):
        return self.icon
