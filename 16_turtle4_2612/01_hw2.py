from turtle import *

t = Turtle()

x = 0
y = 0
length = 50
t.up()
t.goto(x, y)
t.down()
for i in range(3):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.rt(90)

done()
