from tkinter import *

root = Tk()

#set size of input box and color
e = Entry(root, width=50, bg='grey')
e.pack()
#default text inside the input box
e.insert(0, 'enter your name: ')

#get the input of input box
#      e.get()

#printing the input
def myclick():
     #this time we use parenthesis beacuse it is not a function which is defined before
     lab = Label(root,text=e.get())
     lab.pack()

but = Button(root,text='click me',command=myclick)
but.pack()


root.mainloop()