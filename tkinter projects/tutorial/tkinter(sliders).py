from tkinter import *
from PIL import ImageTk,Image

root = Tk()
#set the size of our window
root.geometry("400x400")

vertical = Scale(root , from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack( )

horizontal.get()

def horget():
    lbl = Label(root,text=horizontal.get( ))
    lbl.pack()

btn = Button(root,text="click me!",command=horget).pack()


root.mainloop()