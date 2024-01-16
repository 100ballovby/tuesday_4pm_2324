import random as r

lst1 = []
for i in range(50):
    lst1.append(r.randint(1, 100))

print(lst1)

maximum = 0
minimum = 0
for i in range(len(lst1)):
    if lst1[i] > lst1[maximum]:
        maximum = i
    if lst1[i] < lst1[minimum]:
        minimum = i

print('Максимальный: ', lst1[maximum], 'Индекс: ', maximum)
print('Минимальный: ', lst1[minimum], 'Индекс: ', minimum)
