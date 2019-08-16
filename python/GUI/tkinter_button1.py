import tkinter as tk

def clicked(e):
    print("x:{0} y:{1} text:{2}".format(e.x, e.y, e. widget["text"]))

root = tk.Tk()
button0 = tk.Button(root, text="Hello")
button1 = tk.Button(root, text="World")
button0.pack()
button1.pack()
button0.bind("<Button-1>", clicked)
button1.bind("<Button-3>", clicked)
root.mainloop()
