# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def compres(text):
    count = 0
    symbol = txt[0]
    result = ''
    for i in txt:
        if i == symbol:
            count += 1
        else:
            result += str(count) + symbol
            count = 1
            symbol = i
    result += str(count) + symbol
    return result


def recovery(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


txt = input('Введите строку: ')
print(compres(txt))

txt_1 = input('Введите строку: ')
print(recovery(txt_1))
