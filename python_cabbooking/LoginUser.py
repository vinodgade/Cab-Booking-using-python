from tkinter import *
import sqlite3
import os
from tkinter import messagebox

root = Tk()
root.config(background="#02202b")
root.geometry('600x400')
root.title("LOGIN FORM")

UserName = StringVar()
PassWord = StringVar()

def cl2():
    os.system("SignUpUser.py")
def cl():
    nm = UserName.get()
    ps = PassWord.get()
    with sqlite3.connect("Form.db") as db:
        cursor = db.cursor()
    find_user = ("SELECT * FROM Student WHERE FullName = ? AND PassWord = ?")
    cursor.execute(find_user,[(nm),(ps)])
    result = cursor.fetchall()
    if(nm=="" and ps==""):
        messagebox.showerror("Error","INVALID USERNAME Or PASSWORD")
    if result:
        os.system("BookingRequest.py")
    else:
        messagebox.showerror("Error","INVALID USERNAME Or PASSWORD")
    
label_0 = Label(root, text="USER LOGIN",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_0.place(y=30)


label_1 = Label(root, text="USERNAME",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_1.place(x=30,y=130)

entry_1 = Entry(root,width = 30,textvar=UserName,border = 3)
entry_1.place(x=270,y=135)

label_2 = Label(root, text="PASSWORD",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_2.place(x=30,y=180)

entry_2 = Entry(root,width = 30,textvar=PassWord,border = 3)
entry_2.place(x=270,y=185)


Button(root, text='Login',width=25,bg='brown',fg='white',border = 7,command=cl).place(x=240,y=250)
Button(root, text='SignUp',width=25,bg='brown',fg='white',border = 7,command=cl2).place(x=240,y=310)



root.mainloop()
