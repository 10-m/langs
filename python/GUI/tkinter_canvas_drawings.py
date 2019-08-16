import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_rectangle(100, 50, 200, 100, fill="#FFFF00", outline="#0000FF", width=10)
canvas.create_oval(100, 150, 200, 200, fill="#00FF00", outline="#00FFFF", width=5)
canvas.create_line(300, 50, 400, 100, width=3)
canvas.create_text(350, 180, text="Hello", font=("", 30))
#img = tk.PhotoImage(file = 'logo.png')
#canvas.create_image(100, 250, image=img, anchor=tk.NW)
root.mainloop()
