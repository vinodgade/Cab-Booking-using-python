from tkinter import *

root = Tk()
root.config(background="#223B59")
root.geometry('700x500')
root.title("Available Routes")

L=Label(root,text="AVAILABLE ROUTES",bg="#223B59",fg="white",width=20,font=("bold",20)).place(x=0,y=0)

LH= Label(root,text="STARTING",bg="#223B59",fg="white",width=20).place(x=11,y=40)
l1 = Label(root,text="BH-1",bg="#223B59",fg="white",width=20).place(x=11,y=60)
l2 = Label(root,text="BH-4",bg="#223B59",fg="white",width=20).place(x=11,y=80)
l3 = Label(root,text="BH-5",bg="#223B59",fg="white",width=20).place(x=11,y=100)
l4 = Label(root,text="BH-6",bg="#223B59",fg="white",width=20).place(x=11,y=120)
l5 = Label(root,text="BH-7",bg="#223B59",fg="white",width=20).place(x=11,y=140)
l6 = Label(root,text="GH-1",bg="#223B59",fg="white",width=20).place(x=11,y=160)
l7 = Label(root,text="GH-2",bg="#223B59",fg="white",width=20).place(x=11,y=180)
l8 = Label(root,text="UNI_POLIS",bg="#223B59",fg="white",width=20).place(x=11,y=200)
l9 = Label(root,text="LPU GATE",bg="#223B59",fg="white",width=20).place(x=11,y=220)
l10 = Label(root,text="BLOCK-27",bg="#223B59",fg="white",width=20).place(x=11,y=240)
l11 = Label(root,text="BLOCK-55",bg="#223B59",fg="white",width=20).place(x=11,y=260)

RH= Label(root,text="DESTINATION",bg="#223B59",fg="white",width=20).place(x=200,y=40)
R1 = Label(root,text="BH-1",bg="#223B59",fg="white",width=20).place(x=200,y=60)
R2 = Label(root,text="BH-2",bg="#223B59",fg="white",width=20).place(x=200,y=80)
R3 = Label(root,text="BH-3",bg="#223B59",fg="white",width=20).place(x=200,y=100)
R4 = Label(root,text="BH-4",bg="#223B59",fg="white",width=20).place(x=200,y=120)
R5 = Label(root,text="BH-5",bg="#223B59",fg="white",width=20).place(x=200,y=140)
R6 = Label(root,text="BH-6",bg="#223B59",fg="white",width=20).place(x=200,y=160)
R7 = Label(root,text="UNI_POLIS",bg="#223B59",fg="white",width=20).place(x=200,y=180)
R8 = Label(root,text="LPU GATE",bg="#223B59",fg="white",width=20).place(x=200,y=200)
R9 = Label(root,text="LAW GATE",bg="#223B59",fg="white",width=20).place(x=200,y=220)
l10 = Label(root,text="BLOCK-27",bg="#223B59",fg="white",width=20).place(x=200,y=240)
l11 = Label(root,text="BLOCK-55",bg="#223B59",fg="white",width=20).place(x=200,y=260)


t=Label(root,text="From the STARTING point you can select any one option in DESTINATION LIST\n For further fare amount and detail routes you have to open the option booking request",bg="#223B59",fg="white",width=80,height=3).place(x=11,y=290)

root.mainloop()
