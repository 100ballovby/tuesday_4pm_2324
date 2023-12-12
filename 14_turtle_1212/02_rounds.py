from turtle import *

t = Turtle()
t.speed(0)
colormode(255)  # для работы с цветами в RGB-формате
r = 80  # количество красного
g = 65  # количество зеленого
b = 40  # количество синего

circles = int(input('Количество кругов: '))

for i in range(circles):
    t.color(r, g, b)
    t.circle(40)
    t.rt(360 / circles)
    r += 1
    g += 1
    b += 1

done()
