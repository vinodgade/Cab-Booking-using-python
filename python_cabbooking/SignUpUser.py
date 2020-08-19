from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root = Tk()
root.config(background="#02202b")
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
Password = StringVar()
MobileNo=StringVar()
var = IntVar()
c=StringVar()

def login():
   os.system("LoginUser.py")
   

def database():
   messagebox.showinfo("Sumbit","successfully submitted")
   name1=Fullname.get()
   mob1 = MobileNo.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   password = Password.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (ID INTEGER PRIMARY KEY AUTOINCREMENT,Fullname TEXT UNIQUE,PassWord TEXT UNIQUE,Mobile TEXT,Email TEXT,Gender TEXT,country TEXT)')
   cursor.execute('INSERT INTO Student (FullName,PassWord,Mobile,Email,Gender,country) VALUES(?,?,?,?,?,?)',(name1,password,mob1,email,gender,country))
   conn.commit()
   
   
             
label_0 = Label(root, text="NEW USER",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_1.place(x=30,y=130)

entry_1 = Entry(root,border=3,width=30,textvar=Fullname)
entry_1.place(x=240,y=130)


label_pass = Label(root, text="PassWord",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_pass.place(x=20,y=165)

entry_pass = Entry(root,border=3,width=30,textvar=Password)
entry_pass.place(x=240,y=165)


label_no = Label(root,text = "Mobile no.",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_no.place(x=30,y=203)

entry_no = Entry(root,border=3,width=30,textvar=MobileNo)
entry_no.place(x=240,y=203)



label_2 = Label(root, text="Email",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_2.place(x=30,y=240)

entry_2 = Entry(root,border=3,width=30,textvar=Email)
entry_2.place(x=240,y=240)

label_3 = Label(root, text="Gender",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_3.place(x=30,y=290)

Radiobutton(root, text="Male",padx = 5,bg="#02202b",fg="white",font="Helvetica 10 bold italic" ,variable=var, value=1).place(x=235,y=290)
Radiobutton(root, text="Female",padx = 20,bg="#02202b",fg="white",font="Helvetica 10 bold italic" ,variable=var, value=2).place(x=290,y=290)

label_4 = Label(root, text="country",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_4.place(x=30,y=340)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=340)

Button(root, text='Submit',width=20,bg='brown',fg='white',border = 7,command=database).place(x=180,y=405)

Button(root, text='Login',width=20,bg='brown',fg='white',border = 7,command=login).place(x=180,y=455)

root.mainloop()























