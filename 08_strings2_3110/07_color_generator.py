import random as r
import string as st

alphabet = st.digits + st.ascii_uppercase[:6]
print(alphabet)
colors = []  # пустой список для хранения цветов

# TODO: напишите программу, которая спросит
#  у пользователя, сколько цветов ему нужно,
#  сгенерирует ему эти цвета и добавит их в список
#  список нужно вывести
n_colors = int(input('Сколько цветов нужно?'))
for i in range(n_colors):
    color = '#'
    for j in range(6):
        color += r.choice(alphabet)
    colors.append(color)

for color in colors:
    print(color)
