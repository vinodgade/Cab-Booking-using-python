from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("BOOKING REQUEST")
root.configure(background='#02202b')

MobileNo = StringVar()
from_ = StringVar()
to_ = StringVar()
Day = StringVar()
Time = StringVar()
i = 0
j = 0
k = 0

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

def database(fr2):
   global i,j;
   mobileNo = MobileNo.get()
   fr = from_.get()
   to = to_.get()
   day = Day.get()
   time = Time.get()
   
   location = from_.get()
   destination = to_.get()

   if(location=='BH1'):
      i = 0
   elif(location=='BH4'):
      i = 1
   elif(location=='BH5'):
      i = 2
   elif(location=='BH6'):
      i = 3
   elif(location=='BH7'):
      i = 4
   elif(location=='GH1'):
      i = 5
   elif(location=='GH2'):
      i = 6
   elif(location=='UNI_POLIS'):
      i = 7
   elif(location=='LPU-GATE'):
      i = 8
   elif(location=='BLOCK-27'):
      i = 9
   elif(location=='BLOCK-55'):
      i = 10


   if(destination=='BH1'):
      j = 0
   elif(destination=='BH4'):
      j = 1
   elif(destination=='BH5'):
      j = 2
   elif(destination=='BH6'):
      j = 3
   elif(destination=='BH7'):
      j = 4
   elif(destination=='GH1'):
      j = 5
   elif(destination=='GH2'):
      j = 6
   elif(destination=='UNI_POLIS'):
      j = 7
   elif(destination=='LPU-GATE'):
      j = 8
   elif(destination=='BLOCK-27'):
      j = 9
   elif(destination=='BLOCK-55'):
      j = 10

   s2 = "Rs. "
   s3 = str(fr2[i][j])
   result = s2+s3
   label_charges = Label(root, text="Fare",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
   label_charges.place(x=35,y=280)

   label_fare = Label(root,text=result,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
   label_fare.place(x=240,y=280)



   conn = sqlite3.connect('Booking.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS OrderBooking(ID INTEGER PRIMARY KEY AUTOINCREMENT,MobileNo TEXT,Location TEXT,Destination TEXT ,Day TEXT,Time TEXT)')
   cursor.execute('INSERT INTO OrderBooking(MobileNo,Location,Destination,Day,Time) VALUES(?,?,?,?,?)',(mobileNo,fr,to,day,time))
   conn.commit()
   
   
             
label_0 = Label(root, text="Booking Request",bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_0.place(x=90,y=53)

label_1 = Label(root, text="MobileNo",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_1.place(x=35,y=130)

entry_1 = Entry(root,textvar=MobileNo,border=5,width=30)
entry_1.place(x=240,y=130)

#font = "Helvetica 16 bold italic

label_4 = Label(root, text="FROM",bg="#02202b",fg="white",font="Helvetica 16 bold italic",width=20)
label_4.place(x=35,y=180)

list1 = ['BH1','BH4','BH5','BH6','BH7','GH1','GH2','UNI_POLIS','LPU-GATE','BLOCK-27','BLOCK-55'];

droplist=OptionMenu(root,from_, *list1)
droplist.config(width=30)
from_.set('SELECT YOUR LOCATION') 
droplist.place(x=240,y=180)

label_5 = Label(root, text="TO",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_5.place(x=35,y=230)

list1 = ['BH1','BH2','BH3','BH4','BH5','BH6','UNI_POLIS','LPU-GATE','LAW-GATE','BLOCK-27'];

droplist=OptionMenu(root,to_, *list1)
droplist.config(width=30)
to_.set('SELECT YOUR DESTINATION') 
droplist.place(x=240,y=230)

label_day = Label(root, text="Day",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_day.place(x=35,y=320)

entry_day = Entry(root,textvar=Day,border=5,width=30)
entry_day.place(x=240,y=320)

label_time = Label(root, text="Time",width=20,bg="#02202b",fg="white",font="Helvetica 16 bold italic")
label_time.place(x=35,y=370)

entry_time = Entry(root,textvar=Time,border=5,width=30)
entry_time.place(x=240,y=370)

Button(root, text='Submit',border=5,width=20,bg='brown',fg='white',command = lambda:database(fr)).place(x=180,y=425)

root.mainloop()























