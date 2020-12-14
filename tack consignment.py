
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 19:38:48 2018

@author: Dhanush Sunny
"""
import sqlite3
#track consignment
"""root=Tk()
root.title("track consignment")
w=Label(root,text='enter consignment number')
w.pack(side=LEFT)
E1 = Entry(root, bd = 5)
#E1.grid(row=1,column=3)
w.pack( )
B = Button(root, text = "find")
B.pack(side=LEFT)"""
from tkinter import *

def leve():
    
    cake=Tk()
    width = 400
    height = 280
    screen_width = cake.winfo_screenwidth()
    screen_height = cake.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    cake.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cake.resizable(0, 0)
    Top = Frame(cake, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(cake, height=200)
    Form.pack(side=TOP, pady=20)

    conn=sqlite3.connect("consignment3.db")
    DATA=conn.execute("SELECT * FROM CONSIGNMENT WHERE C_NUMBER= ?",(c.get()))
    for i in DATA:
        #print(i[0],"\n",i[1],"\n",i[2],"\n",i[3],"\n",i[4],"\n",i[5])
        Label(Top,text="consignment number is:").grid(column=1,row=1)
        Label(Top,text=i[0]).grid(column=2,row=1)
        Label(Top,text="customer name is:").grid(column=1,row=2)
        Label(Top,text=i[1]).grid(column=2,row=2)
        Label(Top,text="from address is:").grid(column=1,row=3)
        Label(Top,text=i[2]).grid(column=2,row=3)
        Label(Top,text="to address is:").grid(column=1,row=4)
        Label(Top,text=i[3]).grid(column=2,row=4)
        Label(Top,text="dispatched date is:").grid(column=1,row=5)
        Label(Top,text=i[4]).grid(column=2,row=5)
        Label(Top,text="delivery date is:").grid(column=1,row=6)
        Label(Top,text=i[5]).grid(column=2,row=6)

    btn_back = Button(Form, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Top.destroy()
    top.deiconify()
def back1():
    top.destroy()
    import page2
top = Tk()
width = 400
height = 300
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top.geometry("%dx%d+%d+%d" % (width, height, x, y))
top.resizable(0, 0)
c=StringVar()
Top = Frame(top, bd=2,bg="thistle",  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(top, bg="thistle",height=260)
Form.pack(side=TOP, pady=20)
top.config(bg="thistle")
Label(Top,text='Track consignment',font=60,bg="thistle").pack()
Label(Form,text='Enter Consignment Number',font=20,bg="thistle").grid(row=2)
e1=Entry(Form,textvariable=c)
e1.grid(row=3,column=0)
B = Button(Form,text = "find",command=lambda:leve())
B.grid(pady=25, row=4, columnspan=2)
B.bind('<Return>',leve)
B1 = Button(Form,text = "back",command=lambda:back1())
B1.grid(pady=25, row=5, columnspan=2)
B1.bind('<Return>',back1)

mainloop()

