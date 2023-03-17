from Code import Board

if __name__ == '__main__':
    Board.instantiate_board()
    Board.display_board()
    player_turn = input('Ваш ход? (буква/число):')
    col_start, row_start = Board.algebraic_to_index(player_turn[:2])
    col_end, row_end = Board.algebraic_to_index(player_turn[2:])
    slot = Board.board[col_start][row_start]
    if slot is not None:
        if slot.process_move(col_end, row_end):
            Board.handle_visual_changes(row_start, col_start, row_end, col_end)

    Board.display_board()


