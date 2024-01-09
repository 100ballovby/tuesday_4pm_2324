from turtle import *

angle = int(input('Введите количество углов: '))

t = Turtle()
t.speed(0)

length = 3
for i in range(36):
    t.fd(length)
    t.rt(360 / angle)
    length += 4

done()
