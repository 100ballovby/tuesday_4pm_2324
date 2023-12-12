from turtle import *

t = Turtle()
t.speed(0)

house_x = -150
house_y = 80
width = 160

# дом
t.up()
t.goto(house_x, house_y)
t.down()
t.fillcolor("#a18768")
t.begin_fill()
for i in range(4):
    t.fd(width)
    t.rt(90)
t.end_fill()

t.bk(width * 0.08)
# крыща
t.fillcolor('#a17668')
t.begin_fill()
for i in range(3):
    t.fd(width + (width * 0.08) * 2)
    t.lt(120)
t.end_fill()

# окно
t.up()
t.goto(house_x + (width * 0.1), house_y - (width * 0.25))
t.down()
t.fillcolor('#fff987')
t.begin_fill()
for i in range(4):
    t.fd(width * 0.35)
    t.rt(90)
t.end_fill()

t.up()
t.goto(house_x + (width * 0.6), house_y - (width * 0.25))
t.down()
t.fillcolor('#301c10')
t.begin_fill()
for i in range(2):
    t.fd(width * 0.3)
    t.rt(90)
    t.fd(width * 0.75)
    t.rt(90)
t.end_fill()

done()
