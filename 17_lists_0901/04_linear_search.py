import random as r

lst1 = []
for i in range(20):
    lst1.append(r.randint(1, 100))

print(lst1)

key = int(input('Введите число для поиска: '))
for i in range(len(lst1)):
    if lst1[i] == key:
        print('Нашел на индексе ', i)
        break
