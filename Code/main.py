from Code import Board
from Code.Figures import King

if __name__ == '__main__':
    Board.instantiate_board()
    Board.display_board()

    is_game_finished = False
    is_white = True
    phrase = ['черных', 'белых']
    colors = ['black', 'white']
    while not is_game_finished:
        player_turn = input(f'Ход {phrase[is_white]} (буква/число)')
        col_start, row_start = Board.algebraic_to_index(player_turn[:2])
        col_end, row_end = Board.algebraic_to_index(player_turn[2:])
        slot = Board.board[col_start][row_start]
        if slot is not None:
            if slot.process_move(col_end, row_end, colors[is_white]):
                Board.handle_visual_changes(row_start, col_start, row_end, col_end)
                is_white = not is_white
            else:
                print('Невозможно совершить ход')

        Board.display_board()
