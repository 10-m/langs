import tkinter as tk

root = tk.Tk()
for txt in ("Hello","Python","Language"):
    b = tk.Button(root, text=txt)
    b.pack(side=tk.LEFT)
root.mainloop()
