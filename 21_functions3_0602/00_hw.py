def square(a, b):
    return (a * b)


def str_len(string):
    count = 0
    for letter in string:
        if letter.isalpha():  # если конкретный символ из строки входит в алфавит
            count += 1  # считаем его буквой
    return count


print(square(45, 170))
print(str_len('Hello, Andrew!'))
