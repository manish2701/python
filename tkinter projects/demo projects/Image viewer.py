from tkinter import *
from PIL import ImageTk,Image

root = Tk()


my_img1 = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/images/image1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/images/image2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/images/image3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/Users/manish/Documents/python/tkinter projects/images/image4.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]


#                                                                   new stuff here
Status = Label(root,text="image 1 of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(img_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number-1])

    button_forward = Button(root,text=">>",command=lambda:forward(img_number + 1))
    button_back = Button(root,text="<<",command=lambda:back(img_number - 1))

    if img_number == 4:
        button_forward = Button(root,text=">>",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    #update the status bar
    Status = Label(root,text="image " + str(img_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    Status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(img_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number-1])

    button_forward = Button(root,text=">>",command=lambda:forward(img_number + 1))
    button_back = Button(root,text="<<",command=lambda:back(img_number - 1))

    if img_number == 1:
        button_back = Button(root,text="<<", state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    #update the status bar                                                              new stuff here
    Status = Label(root,text="image " + str(img_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    Status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root,text='<<',command=back, state=DISABLED)
button_quit = Button(root,text='Exit Programm',command=root.quit)
button_forward = Button(root,text='>>',command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
#                                       new stuff here west to east
Status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()