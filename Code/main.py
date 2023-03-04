from Desk.Board import Board

if __name__ == '__main__':
    board = Board()
    board.display_deck()
    user1 = input("Ваш ход: ")
    board.handle_player_turn(user1)
    board.display_deck()
