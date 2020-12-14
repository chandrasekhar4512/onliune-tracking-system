from tkinter import *
root=Tk()
root.title("COURIER MANAGEMENT SYSTEM")
width = 400
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.resizable(0, 0)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

#FRAMES
Top = Frame(root, bd=2,  relief=RIDGE,bg="darkseagreen")
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200,bg="darkseagreen")
Form.pack(side=TOP, pady=20)

def consignment():
    root.destroy()
    import tack_consignment
def Back1():
    root.destroy()
    import INDEX
def cons():
    root.destroy()
    import pickup
root.config(bg="darkseagreen")
    
lbl_home = Label(Top, text="Courier Management System",bg="darkseagreen", font=('times new roman', 20)).pack()
btn_coons=Button(Form,text="consignment tracking",width=45,command=consignment).grid(pady=25,row=0,columnspan=2)
btn_pick=Button(Form,text="place consignment",width=45,command=cons).grid(pady=25,row=3,columnspan=2) 
btn_back = Button(Form, text='Back',width=45 ,command=Back1).grid(pady=25,row=4,columnspan=2)

