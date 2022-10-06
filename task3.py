# Создайте программу для игры в ""Крестики-нолики"".

def print_field(field):
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2])
    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5])
    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8])


def get_winner(field):
    win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_combo:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            return 'Победил "X"'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            return 'Победил "O"'


playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winner = ''


print_field(playing_field)
for i in range(10):
    step = int(input('Введите номер клетки для хода "X": '))
    playing_field[step-1] = 'X'
    print_field(playing_field)
    winner = get_winner(playing_field)
    if winner == 'Победил "X"':
        print(winner)
        break
    step = int(input('Введите номер клетки для хода "O": '))
    playing_field[step-1] = 'O'
    print_field(playing_field)
    winner = get_winner(playing_field)
    if winner == 'Победил "O"':
        print(winner)
        break
