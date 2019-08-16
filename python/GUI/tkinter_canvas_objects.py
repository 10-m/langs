import tkinter as tk

def keyhandler(e):
    r = canvas.coords(ball)
    print(r)
    x, y = 0, 0
    if e.keysym == "Up":
        y = -5
    elif e.keysym == "Down":
        y = +5
    elif e.keysym == "Right":
        x = +5
    elif e.keysym == "Left":
        x = -5
    canvas.move(ball, x, y)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
ball = canvas.create_oval(100, 100, 120, 120, fill="#00FF00") 
root.bind("<Key>", keyhandler)
root.mainloop()
