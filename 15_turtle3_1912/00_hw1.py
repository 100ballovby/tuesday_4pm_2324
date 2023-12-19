from turtle import *

t = Turtle()
t.speed(0)
t.pensize(15)

rad = 50
for i in range(4):
    t.circle(rad)
    t.up()
    t.fd(rad * 1.3)
    t.down()

done()
