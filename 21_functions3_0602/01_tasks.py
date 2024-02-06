def square_list(list_n):
    for i in range(len(list_n)):
        list_n[i] = list_n[i] ** 2


def task2(list_n):
    summary = 0
    length = len(list_n)
    for i in range(length):
        summary += list_n[i]
    return summary / length


def task5(list_n):
    new_list = []
    for i in range(len(list_n)):
        if list_n[i] % 3 == 0:
            new_list.append(list_n[i])
    return new_list


def task3(l1, l2):
    new_list = []
    if len(l1) >= len(l2):
        search_list = l2
    else:
        search_list = l1
    for i in range(len(search_list)):
        if search_list[i] in l1 and search_list[i] in l2:
            new_list.append(search_list[i])
    return new_list


def task4(string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_string = ""
    for symbol in string:
        if symbol.isalpha():
            # symbol = str(ord(symbol.upper()) - ord('A') + 1) + ' '
            symbol = str(alphabet.index(symbol.upper()) + 1) + ' '
        new_string += symbol
    return new_string


l = [3, 12, 5, 14, 7, 91, 34, 65, 15, 21]
l2 = [90, 89, 12, 8, 91, 34, 78, 62, 11, 21, 90, 99, 7]
t2 = task2(l)
t5 = task5(l)
t3 = task3(l, l2)
t4 = task4('Hello, Andrew!')
print(t4)
