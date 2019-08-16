import tkinter as tk

prev = [0, 0]
isMouseDown = False
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def mousemove(event):
    if isMouseDown:
        canvas.create_line(prev[0], prev[1], event.x, event.y)
        prev[0], prev[1] = event.x, event.y

def mousedown(event):
    global isMouseDown
    prev[0], prev[1] = event.x, event.y
    isMouseDown = True

def mouseup(event):
    global isMouseDown
    isMouseDown = False

canvas.bind('<Button-1>' , mousedown)
canvas.bind('<ButtonRelease-1>' , mouseup)
canvas.bind('<Motion>', mousemove)
root.mainloop()
