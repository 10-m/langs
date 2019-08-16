import tkinter as tk
root = tk.Tk()
anchors = [tk.E, tk.W, tk.S]
texts = ["Hello","Python","Language"]
for i in range(3):
    b = tk.Button(root, text=texts[i])
    b.pack(anchor=anchors[i])
root.mainloop()
