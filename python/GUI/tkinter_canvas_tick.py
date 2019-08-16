import tkinter as tk
import collections

keymap = collections.defaultdict(bool)
speed = [0, 0]
MAP = ( (1,1,1,1,1,1,1,1),
        (1,0,1,0,0,0,0,1),
        (1,0,1,0,1,1,0,1),
        (1,0,1,0,0,1,0,1),
        (1,0,1,1,0,1,0,1),
        (1,0,0,0,0,1,0,1),
        (1,1,1,1,1,1,1,1))

def keypress(e):
    keymap[e.keycode] = True

def keyup(e):
    keymap[e.keycode] = False

def tick():
    if keymap[37]: speed[0] -= 1
    if keymap[39]: speed[0] += 1
    if keymap[38]: speed[1] -= 1
    if keymap[40]: speed[1] += 1
    canvas.move(you, speed[0], speed[1])
    speed[0] *= 0.95
    speed[1] *= 0.95
    b = canvas.coords(you)
    collide = canvas.find_overlapping(b[0], b[1], b[2], b[3])
    if len(collide) <= 1:
        root.after(30, tick)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=350)
canvas.bind_all("<KeyPress>", keypress)
canvas.bind_all("<KeyRelease>", keyup)
canvas.pack()
for j, row in enumerate(MAP):
    for i, col in enumerate(row):
        if MAP[j][i] == 1:
            canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill="#00c")
you = canvas.create_rectangle(70,70,90,90,fill="#F0F")
root.after(30, tick)
root.mainloop()
