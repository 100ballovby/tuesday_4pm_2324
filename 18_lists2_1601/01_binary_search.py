import random as r

lst = []
for i in range(50):
    lst.append(r.randint(-50, 50))

lst.sort()  # массив должен быть отсортирован, потому что иначе поиск работать не будет
print(lst)

start = 0
stop = len(lst) - 1
mid = (start + stop) // 2
key = int(input("Что нужно найти в массиве? "))

while (start <= stop and lst[mid] != key):
    # пока в массиве есть числа или mid не равен искомому значению
    if key < lst[mid]:  # если искомое меньше среднего
        stop = mid - 1  # убираем правую часть И СРЕДНЕЕ ТОЖЕ
    elif key > lst[mid]:  # если искомое больше среднего
        start = mid + 1  # убираем левую часть и СРЕДНЕЕ ТОЖЕ
    mid = (start + stop) // 2

if key != lst[mid]:
    print('Значение в массиве не было найдено!')
else:
    print('Нашел элемент! Позиция:', mid)
