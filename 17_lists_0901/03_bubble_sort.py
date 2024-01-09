import random as r

lst1 = []
for i in range(8):
    lst1.append(r.randint(1, 100))

print(lst1)

for i in range(len(lst1) - 1):
    print('Повторение', i)
    for j in range(len(lst1) - i - 1):
        if lst1[j] > lst1[j + 1]:
            tmp = lst1[j]  # записываю текущее число в отдельную переменную
            lst1[j] = lst1[j + 1]  # записываю следующее число на место текущего
            lst1[j + 1] = tmp  # записываю текущее число на место следующего
        print('\tМассив:', lst1[:len(lst1) - i])

print(lst1)
lst1.reverse()
print(lst1)
