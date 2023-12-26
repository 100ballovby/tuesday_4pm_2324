from turtle import *

t = Turtle()
t.speed(0)

length = 100
y = 0
for i in range(13):
    t.fd(length)
    t.bk(length)
    length *= 0.85
    y -= 10
    t.up()
    t.goto(0, y)
    t.down()

done()
