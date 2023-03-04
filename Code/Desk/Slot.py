class Slot:
    def __init__(self, x, y, figure=None):
        self._symbol = '▓' if (x + y) % 2 == 0 else '░'
        self._is_occupied = False
        self._position = [x, y]
        self._figure = figure

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, value):
        self._figure = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if any([0 > i or i < 7 for i in value]):
            raise ValueError("Value must be between 0 and 7")
        self._position = value

    def __repr__(self):
        if self.figure is None:
            return self._symbol
        return str(self.figure)
