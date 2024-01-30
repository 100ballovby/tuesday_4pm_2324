from staff import fill_list


def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:  # если элемент списка совпадает по значению с key
            return i  # вызов return останавливает работу функции
    return -1  # если условие в цикле ни разу не сработает, вернется -1


list_n = fill_list(50, 1, 100)
print(list_n)
res = linear_search(list_n, 30)
if res >= 0:
    print('Element found at index', res)
else:
    print('Element not found')
