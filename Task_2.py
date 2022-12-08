# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Подумайте как наделить бота ""интеллектом""

from random import randint as rnd

count_of_candy = 150
take_candy = 0

def check_player():
    random_number = rnd(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()

def player_turn():
    global count_of_candy
    global take_candy
    print(f'Твой ход! Сейчас на столе {count_of_candy} конфет')
    take_candy = int(input('Сколько возьмешь? '))
    while take_candy < 1 or take_candy > 28 or take_candy > count_of_candy:
        take_candy = int(input('Попробуй снова '))
    count_of_candy -= take_candy
    if count_of_candy > 0:
        bot_turn()
    else:
        print('Ты победил!')

def bot_turn():
    global take_candy
    global count_of_candy
    if count_of_candy % 29 != 0:
        take_candy = count_of_candy % 29
    else:
        take_candy = rnd(1, 28)
    count_of_candy -= take_candy
    print(f'Бот взял {take_candy} конфет. На столе осталось {count_of_candy} конфет.')
    if count_of_candy > 0:
        player_turn()
    else:
        print('Бот победил!')


print('На столе лежит 150 конфет.\nИгроки поочереди берут со стола конфеты, но не более чем 28 за один ход.\n'
      'Первый ход определяется жеребьёвкой.\nВыигрывает тот, кто сделает последний ход.')
print()
check_player()

