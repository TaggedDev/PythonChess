from abc import ABC, abstractmethod


class ChessPiece(ABC):
    @abstractmethod
    def process_move(self, x_end, y_end):
        pass
