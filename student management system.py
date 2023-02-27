from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")

        title = Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)


        #===============Manage Frame===============
        manage_frame = Frame(self.root,bg="crimson",bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=100,width=450,height=640)

        m_title = Label(manage_frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,padx=100,pady=20)



        lbl_roll = Label(manage_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll = Entry(manage_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")



        lbl_name = Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name = Entry(manage_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")



        lbl_email = Label(manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email = Entry(manage_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")



        lbl_gender = Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender = ttk.Combobox(manage_frame,font=("times new roman",14,"bold"),state='readonly')
        combo_gender['values'] = ('male','female','others')
        combo_gender.grid(row=4,column=1,padx=20,pady=10)



        lbl_contact = Label(manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact = Entry(manage_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")



        lbl_dob = Label(manage_frame,text="DOB",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob = Entry(manage_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")



        lbl_address = Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_address = Text(manage_frame,width=21,height=5,font=("",15))
        txt_address.grid(row=7,column=1,padx=20,pady=10,sticky='w')

        #===============Button Frame===============
        btn_frame = Frame(manage_frame,bg="crimson",bd=4,relief=RIDGE)
        btn_frame.place(x=10,y=565,width=420)

        addbtn = Button(btn_frame,text="Add",width=5).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,text="Update",width=5).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,text="Delete",width=5).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_frame,text="Clear",width=5).grid(row=0,column=3,padx=10,pady=10)

        #===============Detail Frame===============
        detail_frame = Frame(self.root,bg="crimson",bd=4,relief=RIDGE)
        detail_frame.place(x=500,y=100,width=830,height=640)

        lbl_search = Label(detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=20,padx=20,sticky="w")

        combo_search = ttk.Combobox(detail_frame,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values'] = ('Roll no.','Name','Contact')
        combo_search.grid(row=0,column=1,padx=20,pady=20)

        txt_search = Entry(detail_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(detail_frame,text="Search",width=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(detail_frame,text="Show all",width=5).grid(row=0,column=4,padx=10,pady=10)

        #================Table Frame================
        table_frame = Frame(detail_frame,bg="crimson",bd=4,relief=RIDGE)
        table_frame.place(x=10,y=70,width=800,height=550)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)
        Student_table=ttk.Treeview(table_frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)

        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")
        Student_table['show'] = 'headings'

        Student_table.column("roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=150)

        Student_table.pack(fill=BOTH,expand=1)

root = Tk()
ob = Student(root) 
root.mainloop()