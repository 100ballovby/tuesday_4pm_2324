from turtle import *

t = Turtle()
t.speed(0)

length = 100
y = 0
x = 0
for i in range(10):
    t.fd(length)
    t.bk(length)
    length -= 10
    y += 10
    x += 5
    t.up()
    t.goto(x, y)
    t.down()

done()
