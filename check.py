from tkinter import *
def d():
    print("mani")
root=Tk()
root.geometry("1300x1200+0+0")

Checkbutton(root,text="mani",command=d).place(x=100,y=100)

root.mainloop()
