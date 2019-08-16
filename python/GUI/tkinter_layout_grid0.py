import tkinter as tk

root = tk.Tk()
for i in range(12):
    button = tk.Button(root, text=i, width=4, font=("",25))
    button.grid(row=i//4, column=i%4, padx=1, pady=2)
root.mainloop()
