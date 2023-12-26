from turtle import *

t = Turtle()
t.speed(0)

length = 3
for i in range(36):
    t.fd(length)
    t.rt(90)
    length += 4

done()
