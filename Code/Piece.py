from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color, x, y):
        self.position = x, y
        self.color = color

    @abstractmethod
    def process_move(self, x_end, y_end, is_white):
        pass

    def update_position(self, y, x):
        self.position = x, y
