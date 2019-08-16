import tkinter as tk
def clicked():
    print("clicked")
root = tk.Tk()
button0 = tk.Button(root, text="Hello", command=clicked)
button1 = tk.Button(root, text="World", command=clicked)
button0.pack()
button1.pack()
root.mainloop()
