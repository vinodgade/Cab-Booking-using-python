from tkinter import *
import os

root = Tk()
root.config(background="#223B59")
root.geometry('1000x200')
root.title("Cab Booking")

def log():
    os.system("LoginUser.py")

def signUp():
    os.system("SignUpUser.py")

def available():
    os.system("available.py")
    
label_0 = Label(root,text="HOME PAGE",bg="#223B59",fg="white",width=20,font=("bold",20))
label_0.place(x=0,y=20)

Button(root,text = "USER LOGIN",border=10,width = 20,height = 3,bg='brown',fg='white',command=log).place(x=100,y=90)
Button(root,text = "NEW USER",border=10,width = 20,height = 3,bg='brown',fg='white',command=signUp).place(x=300,y=90)
Button(root,text = "AVAILABLE ROUTES",border=10,width = 20,height = 3,bg='brown',fg='white',command=available).place(x=500,y=90)

root.mainloop()
