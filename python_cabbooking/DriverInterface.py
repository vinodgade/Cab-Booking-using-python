from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.config(background="#02202b")
root.geometry('500x500')
root.title("DRIVER INTERFACE")
ID = IntVar()
MobileNo = StringVar()
from_ = StringVar()
to_ = StringVar()
Day = StringVar()
Time = StringVar()
a = 0
b = 0
fr = [[0,5,5,5,5,10,10,10,20,15,12],
      [5,0,2,2,5,10,10,10,25,22,17],
      [5,2,0,2,2,10,10,10,30,25,2],
      [15,7,2,0,2,20,20,20,35,30,10],
      [5,10,15,15,0,15,15,15,30,27,32],
      [10,15,25,25,20,0,5,5,15,20,30],
      [10,15,25,25,20,5,0,5,20,15,23],
      [10,15,25,25,20,10,15,0,17,32,22],
      [20,25,30,30,27,15,15,15,0,10,35],
      [11,15,37,40,11,15,30,15,22,0,33],
      [12,22,33,12,20,25,17,18,19,14,0]]
  
with sqlite3.connect("Booking.db ") as db:
    cursor = db.cursor()
cursor.execute("SELECT * FROM OrderBooking WHERE ID = (SELECT MIN(ID) FROM OrderBooking)")
result = cursor.fetchall()
if(result):
    for i in result:
        ID = i[0]
        MobileNo = i[1]
        from_ = i[2]
        to_ = i[3]
        Day = i[4]
        Time = i[5]
else:
    messagebox.showwarning("BOOKING ALERT","No Booking Found")
   

if(from_=='BH1'):
      a = 0
elif(from_=='BH4'):
      a = 1
elif(from_=='BH5'):
      a = 2
elif(from_=='BH6'):
      a = 3
elif(from_=='BH7'):
      a = 4
elif(from_=='GH1'):
      a = 5
elif(from_=='GH2'):
      a = 6
elif(from_=='UNI_POLIS'):
      a = 7
elif(from_=='LPU-GATE'):
      a = 8
elif(from_=='BLOCK-27'):
      a = 9
elif(from_=='BLOCK-55'):
      a = 10


if(to_=='BH1'):
      b = 0
elif(to_=='BH4'):
      b = 1
elif(to_=='BH5'):
      b = 2
elif(to_=='BH6'):
      b = 3
elif(to_=='BH7'):
      b = 4
elif(to_=='GH1'):
      b = 5
elif(to_=='GH2'):
      b = 6
elif(to_=='UNI_POLIS'):
      b = 7
elif(to_=='LPU-GATE'):
      b = 8
elif(to_=='BLOCK-27'):
      b = 9
elif(to_=='BLOCK-55'):
      b = 10

s2 = "Rs. "
s3 = str(fr[a][b])
result = s2+s3
label_charges = Label(root, text="Fare",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_charges.place(x=30,y=280)

label_fare = Label(root,text=result,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_fare.place(x=240,y=280)



   
   
   
             
label_0 = Label(root, text="Driver Interface",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_0.place(x=90,y=53)

label_1 = Label(root, text="MobileNo",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_1.place(x=40,y=130)

label_no = Label(root,text=MobileNo,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_no.place(x=240,y=130)

label_4 = Label(root, text="LOCATION",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_4.place(x=30,y=180)

label_loc = Label(root,text=from_,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_loc.place(x=240,y=180)

label_5 = Label(root, text="DESTINATION",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_5.place(x=20,y=230)

label_dest = Label(root,text=to_,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_dest.place(x=240,y=230)

label_day = Label(root, text="Day",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_day.place(x=30,y=320)

entry_day = Label(root,text = Day,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
entry_day.place(x=240,y=320)

label_time = Label(root, text="Time",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_time.place(x=30,y=370)

entry_time = Label(root,text=Time,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
entry_time.place(x=240,y=370)

def on():
    with sqlite3.connect("Booking.db ") as db:
        cursor = db.cursor()
    cursor.execute("DELETE FROM OrderBooking WHERE ID = (SELECT MIN(ID) FROM OrderBooking)")
    db.commit()
    cursor.close()
    label_no.config(text="-----")
    label_loc.config(text="-----")
    label_dest.config(text="-----")
    entry_day.config(text="-----")
    entry_time.config(text="-----")
    label_fare.config(text="-----")
    
Button(root, text='ON THE WAY',width=20,border = 10,command = on,bg='brown',fg='white').place(x=180,y=425)

root.mainloop()























