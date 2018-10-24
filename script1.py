from tkinter import*

window=Tk()


#=======================================================================================================


Titletxt= StringVar()
Yeartxt= StringVar()
Authortxt= StringVar()
ISBNtxt= StringVar()

#======================================================================================================

L1=Label(window,text="Title")
L1.grid(row=0,column=0)
T1=Entry(window,textvariable=Titletxt)
T1.grid(row=0,column=1)

L2=Label(window,text="Year")
L2.grid(row=1,column=0)
T2=Entry(window,textvariable=Yeartxt)
T2.grid(row=1,column=1)

L3=Label(window,text="Author")
L3.grid(row=0,column=2)
T3=Entry(window,textvariable=Authortxt)
T3.grid(row=0,column=3)

L4=Label(window,text="ISBN")
L4.grid(row=1,column=2)
T4=Entry(window,textvariable=ISBNtxt)
T4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=5,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

B1=Button(window,text="View all",width=12)
B1.grid(row=2,column=3)
B2=Button(window,text="Search entry",width=12)
B2.grid(row=3,column=3)
B3=Button(window,text="Add entry",width=12)
B3.grid(row=4,column=3)
B4=Button(window,text="Update selected",width=12)
B4.grid(row=5,column=3)
B5=Button(window,text="Delete selected",width=12)
B5.grid(row=6,column=3)
B6=Button(window,text="Close",width=12)
B6.grid(row=7,column=3)

window.mainloop()
