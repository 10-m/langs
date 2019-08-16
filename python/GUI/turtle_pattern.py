from turtle import *
from math import sin, cos, radians

def draw_poly(x, y, s, n):
    up()
    setpos(x, y)
    down()
    for _ in range(n):
        fd(s)
        left(360/n)
speed(0)
colormode(1)

for i in range(90):
    rad = radians(i*4)
    r = (sin(rad) + 1) / 2
    g = (cos(rad) + 1) / 2
    b = (sin(rad*2) + 1) / 2

    pencolor(r, g, b)
    draw_poly(0, 0, 100, 4)
    right(4)
done()
