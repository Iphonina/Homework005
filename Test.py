# Создайте программу для игры в ""Крестики-нолики"".
from random import randint as rnd

print(f'Добро пожаловать в игру "Крестики-нолики"! \nТы играешь с ботом и твой ход -"X", ход бота - "O"')
tablo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = chr(10060)
o = chr(11093)
# xo = x


def show_tablo(list):
    print('-' * 13)
    print(f'| {tablo[0]} | {tablo[1]} | {tablo[2]} |')
    print(f'| {tablo[3]} | {tablo[4]} | {tablo[5]} |')
    print(f'| {tablo[6]} | {tablo[7]} | {tablo[8]} |')
    print('-' * 13)


def player_turn():
    while True:
        global x
        turn = int(input(f'Твой ход {x}: '))
        if turn in tablo:
            tablo[turn - 1] = x
            show_tablo(tablo)
            if check_win(x, tablo):
                print(f'{x} - победили!')
                break
            elif draw(tablo):
                print(f'Ничья!')
                break
            bot_turn()
        else:
            print('Неверный ввод, попробуйте еще раз: ')
            continue



def bot_turn():
    while True:
        global o
        print(f'Бот сделал свой ход {o}')
        turn = rnd(1, 9)
        if turn in tablo:
            tablo[turn - 1] = o
            show_tablo(tablo)
            if check_win(o, tablo):
                print(f'{o} - победили!')
                break
            elif draw(tablo):
                print(f'Ничья!')
                break
            player_turn()
        else:
            continue


def check_player():
    check = rnd(0, 1)
    if check == 1:
        player_turn()
    else:
        bot_turn()


def check_win(str, list):
    win_var = (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    for i in win_var:
        for j in i:
            if list[j] == str:
                continue
            else:
                break
        else:
            return True
    else:
        return False


def draw(list):
    for i in range(1, 10):
        if i in list:
            return False
    return True


show_tablo(tablo)
check_player()



