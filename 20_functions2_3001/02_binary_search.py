from staff import fill_list, sort_list


def binary_search(l, key):
    start = 0
    stop = len(l) - 1
    mid = (start + stop) // 2
    while start <= stop:
        if key < l[mid]:
            stop = mid - 1
        elif key > l[mid]:
            start = mid + 1
        else:
            return mid  # return останавливает выполнение функции
        mid = (start + stop) // 2
    return -1


my_list = fill_list(100, -100, 100)
sort_list(my_list)
print(my_list)
res = binary_search(my_list, 30)
if res >= 0:
    print('Element found at index', res)
else:
    print('Element not found')
