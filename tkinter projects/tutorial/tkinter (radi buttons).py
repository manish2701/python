from tkinter import *
from PIL import ImageTk,Image

root = Tk()

# r = intVar()
# r.set("2")

MODES = [
    ("pepparoni","pepparoni"),
    ("cheese","cheese"),
    ("mushroom","mushroom"),
    ("onion","onion"),
]

pizza = StringVar()
pizza.set("pepparoni")

for text,mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    mylabel = Label(root,text=value)
    mylabel.pack()

#making a radio button
# Radiobutton(root, text="option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
# Radiobutton(root, text="option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

#value can be get by label
# mylabel = Label(root,text=pizza.get())
# mylabel.pack()

#value a=can also be get by using button
but = Button(root,text="click me",command=lambda:clicked(pizza.get()))
but.pack()


root.mainloop()