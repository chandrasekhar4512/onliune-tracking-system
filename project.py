from tkinter import *
from tkinter import messagebox
w=Tk()
width = 600
height = 600
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
w.geometry("%dx%d+%d+%d" % (width, height, x, y))
w.resizable(0, 0)
Top = Frame(w, bd=2,  relief=RIDGE,bg="lightpink")
Top.pack(side=TOP, fill=X)
Form = Frame(w, height=500,bg="lightpink")
Form.pack(side=TOP, pady=20)
Top1 = Frame(w, bd=2,  relief=RIDGE)
Top1.pack(fill=X)
Form1 = Frame(w, height=500,bg="lightpink")
Form1.pack(pady=20)
w.config(bg="lightpink")
def s():
    w.destroy()
    import pickup
lbl_title=Label(Top,text="rate calculator",font=('arial',15),bg="lightpink")
lbl_title.pack(fill=X)

Label(Form,text='TO',bg="lightpink").grid(row=0)
Label(Form,text='FROM',bg="lightpink").grid(row=1)
e1=Entry(Form)
e2=Entry(Form)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
ds=IntVar()
wt=IntVar()
ans=StringVar()
amount=IntVar()
C=StringVar()
ex=StringVar()
cvv=StringVar()
l1=Label(Form,text="Distance(KM)",fg="black",bg="lightpink").grid(row=2,column=0)
e1=Entry(Form,border=1,textvariable=ds).grid(row=2,column=1)

l2=Label(Form,text="Weight(KG)",fg="black",bg="lightpink").grid(row=3,column=0)
e2=Entry(Form,border=1,textvariable=wt).grid(row=3,column=1)
button=Button(Form,text="click",command=lambda:mul()).grid(row=4,column=1)
a=ds
b=wt

l1=Label(Form,text="Amount",fg="black",bg="lightpink").grid(row=5,column=0)
e1=Entry(Form,border=1,textvariable=ans).grid(row=5,column=1)
Label(Top1,text="Payment Details",font=('arial',15),bg="lightpink").pack(fill=X)
l2=Label(Form1,text="Amount",fg="black",bg="lightpink").grid(row=5,column=0)
e2=Entry(Form1,border=1,textvariable=ans).grid(row=5,column=1)
l2=Label(Form1,text="Enter credit/debit card number",fg="black",bg="lightpink").grid(row=6,column=0)
e2=Entry(Form1,border=1,show="X",textvariable=C).grid(row=6,column=1)
l2=Label(Form1,text="Enter expiry date",fg="black",bg="lightpink").grid(row=7,column=0)
e2=Entry(Form1,border=1,textvariable=ex).grid(row=7,column=1)
l2=Label(Form1,text="Enter CVV",fg="black",bg="lightpink").grid(row=8,column=0)
e2=Entry(Form1,border=1,show='*',textvariable=cvv).grid(row=8,column=1)
button1=Button(Form1,text="make payment",command=lambda:d()).grid(row=9,column=1)
button2=Button(Form1,text="Back",command=s).grid(row=10,column=1)
def mul():
    ans.set((ds.get())*(wt.get())*0.1)
def d():
    if(ans.get()== "" and C.get()== "" and ex.get()== "" and cvv.get()==""):
      messagebox.showerror("error","Payment failed!")
    else:
        messagebox.showinfo("Payment","payment successfull!")
    
