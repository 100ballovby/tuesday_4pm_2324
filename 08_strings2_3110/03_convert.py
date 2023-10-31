"""Конвертируйте строку в upper(), если она содержит хотя
бы 2 большие буквы в первых четырх буквах"""

word = input('Введите слово: ')
num_upper = 0
for letter in word[:4]:
    if letter.isupper():
        num_upper += 1

    if num_upper >= 2:
        new = word.upper()
        print(new)
    else:
        print(word)
