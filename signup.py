from tkinter import*
from tkinter import messagebox
import os
import sqlite3
def database():
    name1=name.get()
    regno=regn.get()
    email=eid.get()
    mobile=mbl.get()
    gnr=gen.get()
    pswd=password.get()
    conn=sqlite3.connect("Create_form1.db")
    conn.execute("create table IF NOT EXISTS new_form35(name varchar(50),regn varchar(20),eid varchar(20),mbl varchar(20),gen text,pswd varchar(45));")
    conn.execute("insert into new_form35(name,regn,eid,mbl,gen,pswd)values(?,?,?,?,?,?)",(name1,regno,email,mobile,gnr,pswd))
    c=conn.execute("select * from new_form35")
    for i in c:
        print("name1",i[0])
        print("regno",i[1])
        print("email",i[2])
        print("mobile",i[3])
        print("gnr",i[4])
        print("pswd",i[5])
        conn.commit()
    messagebox.showinfo("account","Account Succesfully Created!")
f1=Tk()
width = 1000
height = 720
screen_width = f1.winfo_screenwidth()
screen_height = f1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
f1.geometry("%dx%d+%d+%d" % (width, height, x, y))
f1.resizable(0, 0)

def change_background():
     canvas.itemconfig(myimg,image = gif1)
canvas = Canvas(width =1000, height =700)
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'bg.gif')
myimg=canvas.create_image(0,0, image = gif1, anchor = NW)
def b1():
    f1.destroy()
    import INDEX

name=StringVar()
regn=StringVar()
gen=IntVar()
mbl=StringVar()
eid=StringVar()
password=StringVar()
f1.title("new user interface")
l1=Label(f1,text="Name",font=('arial',20,'bold'),fg="black").place(x=500,y=150)
Entry(f1,bd=3,textvar=name,insertwidth=6).place(x=800,y=150)

l2=Label(f1,text="Registration no.",font=('arial',20,'bold'),fg="black").place(x=500,y=200)
Entry(f1,bd=3,textvar=regn,insertwidth=6).place(x=800,y=200)

l3=Label(f1,text="Gender",font=('arial',20,'bold'),fg="black").place(x=500,y=250)
Radiobutton(f1,text="Male",font=('arial',10,'bold'),variable=gen,value=0).place(x=800,y=250)
Radiobutton(f1,text="Female",font=('arial',10,'bold'),variable=gen,value=1).place(x=870,y=250)

l4=Label(f1,text="Mobile No.",font=('arial',20,'bold'),fg="black").place(x=500,y=300)
Entry(f1,bd=3,textvar=mbl,insertwidth=6).place(x=800,y=300)

l5=Label(f1,text="Email Id",font=('arial',20,'bold'),fg="black").place(x=500,y=350)
Entry(f1,bd=3,textvar=eid,insertwidth=6).place(x=800,y=350)
l6=Label(f1,text="Password",font=('arial',20,'bold'),fg="black").place(x=500,y=400)
Entry(f1,bd=3,textvar=password,insertwidth=6).place(x=800,y=400)

b=Button(f1,text="Submit",bg="red",fg="yellow",command=database).place(x=500,y=450)
b1=Button(f1,text="Back",bg="green",fg="black",command=b1).place(x=500,y=480)
