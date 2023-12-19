from turtle import *

t = Turtle()
t.speed(0)

t.lt(90)
for i in range(7):
    t.circle(15, 180)
    t.rt(180)

t.up()
t.goto(-15, 0)
t.down()

for i in range(7):
    t.circle(15, -180)
    t.rt(180)

t.up()
t.goto(100, 100)
t.down()

for i in range(4):
    t.circle(15, 180)
    t.rt(90)

t.up()
t.goto(100, -100)
t.down()

for i in range(36):
    t.circle(50)
    t.rt(10)

done()
