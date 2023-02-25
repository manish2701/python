from tkinter import *

root = Tk()

label = Label(root,text='select your dish')
label.pack()


def gujarati():
    label = Label(root,text='you have selected gujarati')
    label.pack()
   
    def sevtom():
        label = Label(root,text='you have selected sev ane tomato')
        label.pack()
    
    def vadapav():
        label = Label(root,text='you have selected vadapav')
        label.pack()

    def khamdhok():
        label = Label(root,text='you have selected khaman and dhokla')
        label.pack()

    dish1 = Button(root,text='sev ane tomato',command=sevtom)
    dish2 = Button(root,text='vadapav',command=vadapav)
    dish3 = Button(root,text='khaman and dhokla',command=khamdhok)

    dish1.pack()
    dish2.pack()
    dish3.pack()


def punjabi():
    label = Label(root,text='you have selected punjabi')
    label.pack()
   
    def veg():
        label = Label(root,text='you have selected veg handi')
        label.pack()
    
    def chhole():
        label = Label(root,text='you have selected chhole bhature')
        label.pack()

    def rajma():
        label = Label(root,text='you have selected rajma rice')
        label.pack()

    dish1 = Button(root,text='veg handi',command=veg)
    dish2 = Button(root,text='chhole bhature',command=chhole)
    dish3 = Button(root,text='rajma rice',command=rajma)

    dish1.pack()
    dish2.pack()
    dish3.pack()


def south():
    label = Label(root,text='you have selected south indian')
    label.pack()
   
    def dosa():
        label = Label(root,text='you have selected dosa')
        label.pack()
    
    def medhu():
        label = Label(root,text='you have selected medhuvada')
        label.pack()

    def idli():
        label = Label(root,text='you have selected idli sambar')
        label.pack()

    dish1 = Button(root,text='dosa',command=dosa)
    dish2 = Button(root,text='medhuvada',command=medhu)
    dish3 = Button(root,text='idli sambar',command=idli)

    dish1.pack()
    dish2.pack()
    dish3.pack()


guj = Button(root,text='gujarati',command=gujarati)
pun = Button(root,text='punjabi',command=punjabi)
south = Button(root,text='south indian',command=south)
guj.pack()
pun.pack()
south.pack()            

root.mainloop()