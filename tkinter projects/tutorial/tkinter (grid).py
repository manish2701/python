from tkinter import *
           
root = Tk()


mylabel1 = Label(root, text='hello world')



#using grid system
# first method to put label
#BETTER OPTION IS TWO STEP PROCESS CREATING IT AND THE PUTTING IT
mylabel1.grid(row=0,column=0)

# second method to put label write it in the end
#not preferable
mylabel2 = Label(root, text='hi my name is manish jain').grid(row=1,column=0)

root.mainloop()