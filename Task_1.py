# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст: ")

# вариант, где ищем "абв":
find = "абв"
result = txt.split(' ')

for words in result:
    if find not in words:
        print(words, end=' ')

# вариант, где ищем 'a', 'б', 'в':
new_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'с' not in i, result))
print(new_list)