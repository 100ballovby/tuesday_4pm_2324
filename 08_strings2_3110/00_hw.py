string = input('Введите строку: ')
count = 0
symbol = input('Введите символ для поиска: ')

for i in range(len(string)):
    if string[i].lower() == symbol:
        count += 1

print(f'В строке {count} символов {symbol}')

# задача 2
# max_letter = string[0]
max_letter = 0
for i in range(len(string)):
    # if string[i] > max_letter:
    if ord(string[i]) > max_letter:  # сравниваем код из ASCII с самым большим найденным кодом
        max_letter = ord(string[i])

print(f'Буква с самым большим кодом: {chr(max_letter)}')

# задача 3
count = 0

for i in range(len(string)):
    if string[i] in ',.!?':
        count += 1

print(f'В строке {count} знаков препинания')
