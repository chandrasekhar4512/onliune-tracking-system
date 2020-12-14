from tkinter import *
import sqlite3
root1=Tk()
root1.title("Courier Mangement System")
#window size
width = 600
height = 600
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
root1.resizable(0, 0)
#database part
def done():
    cust=c_name.get()
    tadd=t_address.get()
    fadd=f_address.get()
    ddate=d_date.get()
    dedate=de_date.get()
    con=cons_number.get()
    c=sqlite3.connect("consignment3.db")
    cursor=c.cursor()
    c.execute('''create table IF NOT EXISTS consignment
            (c_number int primary key NOT NULL,
             NAME  TEXT NOT NULL,
             TO_address CHAR(50) NOT NULL,
             F_address CHAR(50) NOT NULL,
             R_DATE CHAR(15),
             D_DATE CHAR(15))''')
    c.execute("INSERT INTO consignment(c_number,NAME,TO_address,F_address,R_DATE,D_DATE)VALUES(?,?,?,?,?,?)",(con,cust,tadd,fadd,ddate,dedate))
    c.commit()
    data=c.execute("SELECT * FROM consignment")
    for row in data:
     print("c_number",row[0])
     print("name",row[1])
     print("to",row[2])
     print("from",row[3])
     print("R_Date",row[3])
     print("D_Date",row[3],"\n")
    print("table created sucessfully")
    
    c.close()
    root1.destroy()
    import project
def run(runfile):
    with open(runfile,"r") as rnf:
     exec(rnf.read())
def back():
    root1.destroy()
    run('page2.py')
#Frames
Top = Frame(root1, bd=2,bg="burlywood",  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root1,bg="burlywood", height=550)
Form.pack(side=TOP, pady=0)
root1.config(bg="burlywood")
#GUI

c_name=StringVar()
f_address=StringVar()
t_address=StringVar()
d_date=StringVar()
de_date=StringVar()
cons_number=IntVar()
lbl_title=Label(Top,text="Pickup consignment",font=('arial',15),bg="burlywood")
lbl_title.pack(fill=X)
lbl_c=Label(Form,text="customer name",font=('arial',14),bd=15,bg="burlywood").grid(row=0,sticky='e')
labl_f=Label(Form,text="from address",font=('arial',14),bd=15,bg="burlywood").grid(row=1,sticky='e')
labl_t=Label(Form,text="to address",font=('arial',14),bd=15,bg="burlywood").grid(row=2,sticky='e')
labl_d=Label(Form,text="dispatch date",font=('arial',14),bd=15,bg="burlywood").grid(row=3,sticky='e')
labl_de=Label(Form,text="delivery date",font=('arial',14),bd=15,bg="burlywood").grid(row=4,sticky='e')
labl_co=Label(Form,text="consignment number",font=('arial',14),bd=15,bg="burlywood").grid(row=5,sticky='e')
#Entry widgets
customer_name = Entry(Form, textvariable=c_name, font=(14))
customer_name.grid(row=0, column=1)
from_adress= Entry(Form, textvariable=f_address, font=(14))
from_adress.grid(row=1, column=1)
to_adress= Entry(Form, textvariable=t_address, font=(14))
to_adress.grid(row=2, column=1)
dispatch_date= Entry(Form, textvariable=d_date, font=(14))
dispatch_date.grid(row=3, column=1)
delivery_date= Entry(Form, textvariable=de_date, font=(14))
delivery_date.grid(row=4, column=1)
cons_number= Entry(Form, textvariable=cons_number, font=(14))
cons_number.grid(row=5, column=1)
#Button
btn_done = Button(Form, text="proceed to payment", width=45, command=done)
btn_done.grid(pady=25, row=6, columnspan=2)
btn_done.bind('<Return>', done)
btn_back = Button(Form, text="back", width=45, command=back)
btn_back.grid(pady=25, row=7, columnspan=2)
btn_back.bind('<Return>', back)
