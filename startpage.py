from tkinter import*
import random
import os

root = Tk()
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

root.title("Courier Management System")
def signup():
  os.system('signup.py')
def login():
  #os.popen('INDEX.py')

#-----------------INFO TOP------------
lblinfo = Label(root, font=( 'aria' ,18, 'bold' ),text="Courier Management System",fg="steel blue")
lblinfo.place(x=20,y=0)
btn=Button(root,font=('aria',14),text="Login   ",command=login,bg="steel blue")
btn.place(x=80,y=40)
btn_coons=Button(root,text="consignment tracking",command=signup,bg="Green")
btn_coons.place(x=80,y=80)
btn1=Button(root,font=('aria',14),text="About ",bg="Red")
btn1.place(x=80,y=120)
#---------------------------------------------------
