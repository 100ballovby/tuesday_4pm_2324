import math
from turtle import *

t = Turtle()
t.speed(0)
radius = 5
angle = 5
turns = 5
for i in range(turns * 360 // angle):
    t.fd(angle * math.pi / 180 * radius)
    t.lt(angle)
    radius += 0.4

done()
