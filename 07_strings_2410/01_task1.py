phrase = input('Введите фразу: ')
"""
Необходимо написать программу, которая посчитает количество гласных букв в строке
"""
vowels = 'аеёиоуэыюя'
count = 0
for i in range(len(phrase)):
    if phrase[i] in vowels:
        count += 1
print(f'В строке {count} гласных букв.')
