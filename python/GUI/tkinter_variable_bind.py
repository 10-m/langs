import tkinter as tk

def scaleUpdate(e):
    color = "#{0:02x}{1:02x}{2:02x}".format(R.get(), G.get(), B.get())
    root.configure(bg = color)
    
def btnUpdate():
    txt = "radio={0} check={1}".format(RadioVar.get(), CheckVar.get())
    TextVar.set(txt)

root = tk.Tk()
TextVar = tk.StringVar()
label = tk.Label(root, textvariable=TextVar)
label.pack()
R, G, B = tk.IntVar(), tk.IntVar(), tk.IntVar()
for color in [R, G, B]:
    tk.Scale(root, orient = 'h', from_ = 0, to = 255,  variable = color, command = scaleUpdate).pack(fill=tk.X)
RadioVar = tk.IntVar()

for num in range(3):
    tk.Radiobutton(root, text = num, value = num, variable = RadioVar, command = btnUpdate).pack()
CheckVar = tk.BooleanVar()
tk.Checkbutton(root, variable = CheckVar, command = btnUpdate).pack()
root.mainloop()
