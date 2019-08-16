import tkinter as tk

root = tk.Tk()
root.geometry("200x150")
button0 = tk.Button(root, text="Hello")
button1 = tk.Button(root, text="Python")
button2 = tk.Button(root, text="Language")
button0.place(x=10, y=20, width=150, height=30)
button1.place(x=80, y=40, width=100, height=30)
button2.place(relx=0.1, rely=0.6, relwidth=0.3, 
relheight=0.2)
root.mainloop()
