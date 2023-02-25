from tkinter import *

root = Tk()

#we can even use functions
def myclick():
     mylabel = Label(root,text='look i clicked a button')
     mylabel.pack()


#creating a button     command is used to tell what to do when button is pressed 
#here we will run our function myclick without () parenthesis
mybutton = Button(root,text='click me', command=myclick)

#padx and pady decides the length and breadth of the button
mybutton2 = Button(root,text='click me', padx=30,pady=30,)

#change the foreground(text) ang background color of the button
mybutton3 = Button(root,text='click me', bg='yellow' ,fg="blue" )


mybutton.pack()
mybutton2.pack()
mybutton3.pack()

root.mainloop()