import tkinter as tk

def textUpdate():
    label.configure(text=entry.get())

def scaleUpdate(e):
    label.configure(font=("", e))


root = tk.Tk()
label = tk.Label(root)
label.pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Update", command=textUpdate).pack()
tk.Scale(root, orient = 'h', from_ = 10, to = 50,
         command=scaleUpdate).pack(fill=tk.X)
root.mainloop()
