import Board


def validate_algebraic(string):
    if len(string) == 4:
        letters = [string[0], string[2]]
        nums = [string[1], string[3]]
        if all([x.isdigit() for x in nums]) and all([x.isalpha() for x in letters]):
            if all(['a' <= x <= 'h' for x in letters]) and all(['1' <= x <= '8' for x in nums]):
                return True

    return False


def inverse_turn(string):
    return string[2:], string[:2]


if __name__ == '__main__':
    Board.instantiate_board()
    Board.display_board()
    turns = []

    is_game_finished = False
    is_white = True
    phrase = ['черных', 'белых']
    colors = ['black', 'white']
    while not is_game_finished:
        player_turn = input(f'Ход {phrase[is_white]} (буква/число)')

        if validate_algebraic(player_turn):
            col_start, row_start = Board.algebraic_to_index(player_turn[:2])
            col_end, row_end = Board.algebraic_to_index(player_turn[2:])
            slot = Board.board[col_start][row_start]

            if slot is not None:
                if slot.process_move(col_end, row_end, colors[is_white]):
                    Board.handle_visual_changes(row_start, col_start, row_end, col_end)
                    is_white = not is_white
                    turns.append(player_turn)
                else:
                    print('Невозможно совершить ход')

        elif player_turn == '0-0':
            indices = [7, 0]
            is_castling_possible = True
            for i in range(5, 7):
                if Board.board[indices[is_white]][i] is not None:
                    print(f'Ход сделать невозможно, слот {indices[is_white], i} занят')
                    is_castling_possible = False
                elif Board.is_slot_attacked(indices[is_white], i):
                    print(f'Ход сделать невозможно, слот {indices[is_white], i} атакован')
                    is_castling_possible = False

            if is_castling_possible:
                Board.handle_visual_changes_castling(is_white=is_white, type='short')

        elif player_turn == '0-0-0':
            indices = [7, 0]
            for i in range(1, 4):
                if Board.board[indices[is_white]][i] is not None:
                    print('Ход сделать невозможно')
                elif Board.is_slot_attacked(indices[is_white], i):
                    print('Ход сделать невозможно')
                else:
                    Board.handle_visual_changes_castling(is_white=is_white, type='long')


            pass
        elif player_turn == '0-0':
            pass
        elif player_turn == 'redo':
            if len(turns) == 0:
                print(f'Это первый ход')
                continue

            last_turn = turns[-1]
            start, end = inverse_turn(last_turn)
            col_start, row_start = Board.algebraic_to_index(start)
            col_end, row_end = Board.algebraic_to_index(end)
            slot = Board.board[col_start][row_start]
            Board.handle_visual_changes(row_start, col_start, row_end, col_end)
            is_white = len(turns) % 2 == 1
            turns.pop()
            print(f'Откат: {last_turn}')
        else:
            print('Проверьте правильность введённой комбинации')

        Board.display_board()
