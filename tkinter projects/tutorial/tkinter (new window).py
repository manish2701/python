from tkinter import *
from PIL import ImageTk,Image

root = Tk()

"""
to display image either we can set img to a global variable 
or just set the img codeline outside the function
"""

def open():
    #for img to dispplay it has to global variable to a local variable
    global img
    #create another window
    top = Toplevel()
    img = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/images/image1.png"))
    lbl = Label(top,image=img).pack()

    #quit just closes the whole programmm while destroy jus closes that window
    btn2 = Button(top, text="close window", command=top.destroy).pack()



#make it show when button  is pressed
btn = Button(root,text="click me to see the image",command=open).pack()

root.mainloop()