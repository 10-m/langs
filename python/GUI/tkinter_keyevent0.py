import tkinter as tk

def keydown(e):
    label["text"] = "keydown:" + str(e.keycode)

def keyup(e):
    label["text"] = "keyup:" + str(e.keycode)

root = tk.Tk()
label = tk.Label(root)
label.pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text = "hello").pack()
entry.bind("<KeyPress>", keydown)
entry.bind("<KeyRelease>", keyup)
root.mainloop()
