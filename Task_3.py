# Создайте программу для игры в ""Крестики-нолики"".
print(f'Добро пожаловать в игру "Крестики-нолики"! \nТы ходишь -"X", соперник - "O"')
tablo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = chr(10060)
o = chr(11093)
xo = x

def show_tablo(list):
    print('-'*13)
    print(f'| {tablo[0]} | {tablo[1]} | {tablo[2]} |')
    print(f'| {tablo[3]} | {tablo[4]} | {tablo[5]} |')
    print(f'| {tablo[6]} | {tablo[7]} | {tablo[8]} |')
    print('-'*13)

show_tablo(tablo)

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

# if __name__ == "__main__":
while True:
    turn = int(input(f'Xод {xo}: '))
    if turn in tablo:
        tablo[turn - 1] = xo
        show_tablo(tablo)
        if check_win(xo, tablo):
            print(f'{xo} - победили!')
            break
        elif draw(tablo):
            print(f'Ничья!')
            break
        xo = x if xo == o else o
    else:
        print('Неверный ввод, попробуйте еще раз: ')
        continue




