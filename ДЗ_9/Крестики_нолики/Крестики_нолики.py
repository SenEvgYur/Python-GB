from email.mime import image


board = list(range(1, 10))

wins_cords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i*3], '|',
              board[1 + i*3], '|', board[2 + i*3], '|')
    print('-------------')


def take_input(znak):
    while True:
        value = input('Куда поставить: ' +znak + '? ')
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите набор')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = znak
        break


def check_win():
    for item in wins_cords:
        if (board[item[0]-1]) == (board[item[1]-1]) == (board[item[2]-1]):
            return board[item[1]-1]
    else:
        return False


def igra():
    hod = 0
    while True:
        draw_board()
        if hod % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if hod > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'Победа !!!')
                break
        hod += 1
        if hod > 8:
            draw_board()
            print('Ничья')
            break


igra()

