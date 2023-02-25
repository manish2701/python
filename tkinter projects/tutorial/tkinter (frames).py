from tkinter import *

root = Tk()

#how ot create a frame
#this pads the inside of the frame
# text is not necessary you can put or eemove it
frame = LabelFrame(root,padx=50,pady=50)
#this pads the outside of the frame
frame.pack(padx=5,pady=5)

#we want buttonn in frame so use frame at the place of root
b = Button(frame,text="Don't click here")
b.grid(row=0,column=0)

b2 = Button(frame,text="Don't click here")
b2.grid(row=0,column=1)

root.mainloop()