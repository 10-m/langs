import turtle as t
from math import sin, cos, radians

def draw_poly(x, y, s, n):
    t.up()
    t.setpos(x, y)
    t.down()
    for _ in range(n):
        t.fd(s)
        t.left(360/n)

draw_poly(-200, 200, 100, 3)
draw_poly(0, 200, 100, 4)
draw_poly(200, 200, 80, 5)
draw_poly(-200, 0, 75, 6)
draw_poly(0, 0, 70, 7)
draw_poly(200, 0, 50, 8)
draw_poly(-200, -200, 45, 10)
draw_poly(0, -200, 30, 15)
draw_poly(200, -200, 20, 20)
t.done()
