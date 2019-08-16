import tkinter as tk

root = tk.Tk()
params = ("System", 20, "bold", "italic", "underline", 
"overstrike")
for i in range(len(params)):
    s = params[0:i+1]
    tk.Label(root, text=str(s), font=s).pack(fill=tk.X)
root.mainloop()
