from tkinter import *
#import messagebox
from tkinter import messagebox

root = Tk()

"""
types of messageboxes
showinfo     = returns values as   OK 
showwarning  = returns values as   OK
showerror    = returns values as   OK
askquestion  = returns values as   yes &  no
askokcancel  = returns values as   1 & 0
askyesno     = returns values as   1 & 0
"""


#in order to use the messagebox we can put it in a variable and then use it in if statement
def popup():
    response = messagebox.askyesno("this is my popup", "hello world")

    #clicking yes gives a value of 1 and no gives 0
    if response == 1:
        Label(root, text="you clicked yes!").pack()
    else:
        Label(root, text="you clicked no!").pack()


Button(root, text="popup", command=popup).pack()

root.mainloop()