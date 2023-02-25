from tkinter import *
from PIL import ImageTk,Image

root = Tk()
#for icon
# root.iconbitmap("icon url")

#for images
my_img = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/tutorial/tkinter icons/images.png"))
my_label = Label(image=my_img)
my_label.pack()


#for quiting the programm
button_quit = Button(root,text='exit program',command=root.quit)
button_quit.pack()


root.mainloop()