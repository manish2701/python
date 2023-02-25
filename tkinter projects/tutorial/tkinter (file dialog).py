from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir= "/Users/manish/Documents/python/tkinter projects/images",title="select a file", filetypes=(("png files","*.png"),("all files","*.*")))
    #root.filename gives us the whole path of the selected or opened item
    lbl = Label(root,text=root.filename).pack()

    #show that image
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lbl = Label(root,image=my_img).pack()

btn = Button(root,text="choose an image",command=open).pack()


# EXPLAINATION WITH SYNTAX 

#                                                choose start directory                                                             give file type which you have to open and from all file types     
#root.filename = filedialog.askopenfilename(initialdir= "/Users/manish/Documents/python/tkinter projects/images",title="select a file", filetypes=(("png files","*.png"),("all files","*.*")))
#                                                                                                                                                    file name , file type | file name , file type 
#get the info from dialog box                                                                                                             putting all file types is necessary to open a file dialog                                                                   
#root.filename gives us the whole path of the selected or opened item
# lbl = Label(root,text=root.filename).pack()

#show that image
# my_img = ImageTk.PhotoImage(Image.open(root.filename))
# my_img_lbl = Label(root,image=my_img).pack()

root.mainloop()