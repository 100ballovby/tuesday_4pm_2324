"""
Напишем программу, которая генерирует таблицу умножения для
числа, которое введет пользователь:
"""
n = int(input('Введите число: '))
stop = int(input('До какого числа нужна таблица? '))

for i in range(1, stop + 1):
    print(n, '*', i, '=', n * i)


