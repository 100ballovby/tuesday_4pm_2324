import random as r
import string
from turtle import *

colors = []
alphabet = string.hexdigits  # сохранили алфавит 16-ричной системы
for i in range(1000):
    color = '#'
    for j in range(6):
        color += r.choice(alphabet)
    colors.append(color)

print(colors)

t = Turtle()
t.speed(0)

rounds = r.randint(400, 1500)
for i in range(rounds):
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    d = r.randint(40, 90)
    col = r.choice(colors)
    t.color(col)
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(d)

done()
