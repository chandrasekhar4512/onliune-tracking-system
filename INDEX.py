from tkinter import *
import sqlite3
import os

root = Tk()
root.title("COURIER MANAGEMENT SYSTEM")
root.config(bg='palegreen')
#window sizinga
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
global lbl_text
#Database
def Database():
    global conn, cursor
    conn = sqlite3.connect("Create_form1.db")
    cursor = conn.cursor()
    conn.execute("create table IF NOT EXISTS new_form35(name varchar(50),regn varchar(20),eid varchar(20),mbl varchar(20),gen text,pswd varchar(45));")      
    cursor.execute("SELECT * FROM `new_form35`")
    #if cursor.fetchone() is None:
     #   cursor.execute("INSERT INTO `database` (username, password) VALUES('dhanush', 'admin')")
    conn.commit()
    
def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `new_form35` WHERE name = ? AND pswd = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def HomeWindow():
 root.destroy()
 import page2
def run(runfile):
    with open(runfile,"r") as rnf:
     exec(rnf.read())
def Register():
    root.destroy()
    import signup    
#VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()

#FRAMES
Top = Frame(root, bd=2,  relief=RIDGE,bg='palegreen')
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200,bg='palegreen')
Form.pack(side=TOP, pady=20)

#LABELS
lbl_title = Label(Top, text = "Courier Management System", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15,bg='palegreen')
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15,bg='palegreen')
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#ENTRY WIDGETS
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#BUTTON WIDGETs
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)
btn_signup=Button(Form, text="Register",width=45,command=Register)
btn_signup.place(x=1,y=180)
btn_signup.bind('<Return>',Register)
