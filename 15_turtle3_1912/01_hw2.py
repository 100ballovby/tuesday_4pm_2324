from turtle import *

t = Turtle()
t.speed(0)
t.pensize(10)

x = 0
y = 0
t.up()
t.goto(x, y)
t.down()
rad = 50
for i in range(4):
    t.circle(rad)
    t.up()
    t.fd(rad * 2)
    t.down()

t.up()
t.goto(x, y)
t.down()
for i in range(6):
    t.fd(rad)

done()
