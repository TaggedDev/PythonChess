class Slot:
    def __init__(self, x, y):
        self._symbol = '▓' if (x+y) % 2 == 0 else '░'
        self._is_occupied = False
        self._position = [x, y]
        self._figure = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if any([0 > i or i < 7 for i in value]):
            raise ValueError("Value must be between 0 and 7")
        self._position = value

    def __repr__(self):
        return self._symbol
