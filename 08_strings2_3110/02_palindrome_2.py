"""Палиндромы - это слова, которые читаются одинаково слева-направо и справа-налево"""
word = input('Введите слово: ')

"""Нормальное решение представляет собой перебор строки с двух сторон. 
И если буквы одинаковые, то слово будет палиндромом"""
left_border = 0
right_border = len(word) - 1
is_palindrome = True
while left_border <= right_border:
    if word[left_border] != word[right_border]:
        is_palindrome = False
        break
    left_border += 1
    right_border -= 1

if is_palindrome:
    print(f'Слово {word} - это палиндром')
else:
    print(f'Слово {word} не палиндром!')
