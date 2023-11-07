"""
Необходимо написать программу, которая получит от пользователя строчку, а затем
трансформирует строку таким образом, чтобы слова будут написаны в обратном порядке,
но порядок слов должен быть сохранен.
"""

input_string = input('Строка: ')
words = input_string.split()
print(words)

for word in range(len(words)):
    words[word] = words[word][::-1]

result = ' '.join(words)
print(result)
