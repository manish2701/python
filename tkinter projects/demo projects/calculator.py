from tkinter import *

root = Tk()

#input box
text = Entry(root,width=35,borderwidth=5)
text.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
     current = text.get()
     text.delete(0, END)
     text.insert(0, str(current) + str(number))


def button_clear():
     text.delete(0, END)


def button_add():
     first_number = text.get()
     global f_num
     global math
     math = "addition"
     f_num = int(first_number)

     text.delete(0, END)

def button_multiply():
     first_number = text.get()
     global f_num
     global math
     math = "multiplication"
     f_num = int(first_number)

     text.delete(0, END)

def button_divide():
     first_number = text.get()
     global f_num
     global math
     math = "division"
     f_num = int(first_number)

     text.delete(0, END)

def button_subtract():
     first_number = text.get()
     global f_num
     global math
     math = "subtraction"
     f_num = int(first_number)

     text.delete(0, END)

def button_equal():
     second_number = text.get()
     text.delete(0, END)

     if math == "addition":
          text.insert(0, f_num + int(second_number))
     
     if math == "subtraction":
          text.insert(0, f_num - int(second_number))
     
     if math == "multiplication":
          text.insert(0, f_num * int(second_number))
     
     if math == "division":
          text.insert(0, f_num / int(second_number))


#creating button
#lambda is used to input values in an function with int and str both
num1 = Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1))
num2 = Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2))
num3 = Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3))
num4 = Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4))
num5 = Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5))
num6 = Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6))
num7 = Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7))
num8 = Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8))
num9 = Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9))
num0 = Button(root,text='0',padx=38,pady=20,command=lambda:button_click(0))

numclear = Button(root,text='Clear',padx=40,pady=20,command=button_clear)
numequal = Button(root,text='=',padx=101,pady=20,command=button_equal)

numadd = Button(root,text='+',padx=45,pady=20,command=button_add)
numsub = Button(root,text='-',padx=45,pady=20,command=button_subtract)
nummult = Button(root,text='*',padx=45,pady=20,command=button_multiply)
numdiv = Button(root,text='/',padx=45,pady=20,command=button_divide)

#putting button
num1.grid(row=3,column=0)
num2.grid(row=3,column=1)
num3.grid(row=3,column=2)

num4.grid(row=2,column=0)
num5.grid(row=2,column=1)
num6.grid(row=2,column=2)

num7.grid(row=1,column=0)
num8.grid(row=1,column=1)
num9.grid(row=1,column=2)

num0.grid(row=4,column=0)

numclear.grid(row=0,column=3)
numadd.grid(row=1,column=3)
numequal.grid(row=4,column=1,columnspan=2)

numsub.grid(row=2,column=3)
nummult.grid(row=3,column=3)
numdiv.grid(row=4,column=3)

root.mainloop()