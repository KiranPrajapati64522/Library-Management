from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

# ------------------------------------Add Data ------------------------------------------------
def addadata():
    conn=mysql.connector.connect(host="localhost",user="root",password="kiran@1999",database="mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        member_var.get(),
                                                                                                        prn_var.get(),
                                                                                                        id_var.get(),
                                                                                                        firstname_var.get(),
                                                                                                        lastname_var.get(),
                                                                                                        address_var.get(),
                                                                                                        postcode_var.get(),
                                                                                                        mobile_var.get(),
                                                                                                        bookId_var.get(),
                                                                                                        bookTitle_var.get(),
                                                                                                        author_var.get(),
                                                                                                        dateOfBorrowed_var.get(),
                                                                                                        dateOfDue_var.get(),
                                                                                                        daysOnBook_var.get(),
                                                                                                        lateReturnFine_var.get(),
                                                                                                        dateOverDue_var.get(),
                                                                                                        actualPrice_var.get()
                                                                                                    ))
    conn.commit()
    fatch_data()
    conn.close()
    messagebox.showinfo("Succes","Member has been inserted succesfully")

#------------------------------------Fatch Data--------------------------------------------------------
def fatch_data():
    conn=mysql.connector.connect(host="localhost",user="root",password="kiran@1999",database="mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("select*from library")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Library_table.delete(*Library_table.get_children())
        for items in rows:
            Library_table.insert("",END,values=items)
        conn.commit()
    conn.close()

#---------------------------------------get cursor------------------------------------------
def get_cursor(event=""):
    cursor_row=Library_table.focus()
    content=Library_table.item(cursor_row)
    row=content['values']

    member_var.set(row[0])
    prn_var.set(row[1])
    id_var.set(row[2])
    firstname_var.set(row[3])
    lastname_var.set(row[4])
    address_var.set(row[5])
    postcode_var.set(row[6])
    mobile_var.set(row[7])
    bookId_var.set(row[8])
    bookTitle_var.set(row[9])
    author_var.set(row[10])
    dateOfBorrowed_var.set(row[11])
    dateOfDue_var.set(row[12])
    daysOnBook_var.set(row[13])
    lateReturnFine_var.set(row[14])
    dateOverDue_var.set(row[15])
    actualPrice_var.set(row[16])

#-----------------------------------show data------------------------------------------------------
def showData():
    txtBox.insert(END,"Member Type\t\t"+member_var.get()+"\n")
    txtBox.insert(END,"PRN No.\t\t"+prn_var.get()+"\n")
    txtBox.insert(END,"ID No.\t\t"+id_var.get()+"\n")
    txtBox.insert(END,"First Name\t\t"+firstname_var.get()+"\n")
    txtBox.insert(END,"Last Name\t\t"+lastname_var.get()+"\n")
    txtBox.insert(END,"Address\t\t"+address_var.get()+"\n")
    txtBox.insert(END,"PostCode\t\t"+postcode_var.get()+"\n")
    txtBox.insert(END,"Mobile No.\t\t"+mobile_var.get()+"\n")
    txtBox.insert(END,"Book Id\t\t"+bookId_var.get()+"\n")
    txtBox.insert(END,"Book Title\t\t"+bookTitle_var.get()+"\n")
    txtBox.insert(END,"Author\t\t"+author_var.get()+"\n")
    txtBox.insert(END,"Date Of Borrowed\t\t"+dateOfBorrowed_var.get()+"\n")
    txtBox.insert(END,"Date Of Due\t\t"+dateOfDue_var.get()+"\n")
    txtBox.insert(END,"Days On Book\t\t"+daysOnBook_var.get()+"\n")
    txtBox.insert(END,"Late Return Fine\t\t"+lateReturnFine_var.get()+"\n")
    txtBox.insert(END,"Date Over Due\t\t"+dateOverDue_var.get()+"\n")
    txtBox.insert(END,"Actual Price\t\t"+actualPrice_var.get()+"\n")

#------------------------------Reset Data--------------------------------------------------------
def reset():
    member_var.set("")
    prn_var.set("")
    id_var.set("")
    firstname_var.set("")
    lastname_var.set("")
    address_var.set("")
    postcode_var.set("")
    mobile_var.set("")
    bookId_var.set("")
    bookTitle_var.set("")
    author_var.set("")
    dateOfBorrowed_var.set("")
    dateOfDue_var.set("")
    daysOnBook_var.set("")
    lateReturnFine_var.set("")
    dateOverDue_var.set("")
    actualPrice_var.set("")
    txtBox.delete("1.0",END)

#----------------------------------Update data-------------------------------------------------------
def update():
    if prn_var.get()=="" or id_var.get()=="":
        messagebox.showerror("Error","First Select the Member")
    else:   
        conn=mysql.connector.connect(host="localhost",user="root",password="kiran@1999",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID_No=%s,FirstName=%s,LastName=%s,Address=%s,PostCode=%s,MobileNo=%s,BookId=%s,BookTitle=%s,Author=%s,DateOfBorrowed=%s,DateOfDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_No=%s",(
                                                                                                        member_var.get(),
                                                                                                        id_var.get(),
                                                                                                        firstname_var.get(),
                                                                                                        lastname_var.get(),
                                                                                                        address_var.get(),
                                                                                                        postcode_var.get(),
                                                                                                        mobile_var.get(),
                                                                                                        bookId_var.get(),
                                                                                                        bookTitle_var.get(),
                                                                                                        author_var.get(),
                                                                                                        dateOfBorrowed_var.get(),
                                                                                                        dateOfDue_var.get(),
                                                                                                        daysOnBook_var.get(),
                                                                                                        lateReturnFine_var.get(),
                                                                                                        dateOverDue_var.get(),
                                                                                                        actualPrice_var.get(),
                                                                                                        prn_var.get()
                                                                                                    ))
        conn.commit()
        fatch_data()
        reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated.")  

#------------------------------------Delete Data------------------------------------------
def delete():
    if prn_var.get()=="" or id_var.get()=="":
        messagebox.showerror("Error","First Select the Member")
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="kiran@1999",database="mydata")
        my_cursor=conn.cursor()
        query="delete from library where PRN_No=%s"
        value=(prn_var.get(),)
        my_cursor.execute(query,value)

    conn.commit()
    fatch_data()
    reset()
    conn.close()
    messagebox.showinfo("Succes","Member has been Deleted.")

#-------------------------------Exit from the file-----------------------------------------------
def Exit():
    Exit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit ?")
    if Exit>0:
        root.destroy()
        return
#----------------------------given the root to gui ---------------------------------------------
root=Tk() 
root.geometry("1550x800+0+0")
root.title("Library Management System")

        #-----------------------------------Variable------------------------------------------------

member_var=StringVar()
prn_var=StringVar()
id_var=StringVar()
firstname_var=StringVar()
lastname_var=StringVar()
address_var=StringVar()
postcode_var=StringVar()
mobile_var=StringVar()
bookId_var=StringVar()
bookTitle_var=StringVar()
author_var=StringVar()
dateOfBorrowed_var=StringVar()
dateOfDue_var=StringVar()
daysOnBook_var=StringVar()
lateReturnFine_var=StringVar()
dateOverDue_var=StringVar()
actualPrice_var=StringVar()


lb1title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="white",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
lb1title.pack(side=TOP,fill=X)

frame=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
frame.place(x=0,y=130,width=1530,height=400)

        #--------------------------------------------DataFrameleft------------------------------------------------

DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="blue",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameLeft.place(x=0,y=5,width=900,height=350)

lb1Member=Label(DataFrameLeft,text="Member Type:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
lb1Member.grid(row=0,column=0,sticky="w")
comMember= ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),textvariable=member_var,width=27,state="readonly")
comMember["value"]=("Admin Staff","Student","Lecturer")
comMember.grid(row=0,column=1)

lb2PRN_No=Label(DataFrameLeft,text="PRN No.:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb2PRN_No.grid(row=1,column=0,sticky="w")
textPRN_No=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=prn_var)
textPRN_No.grid(row=1,column=1)

lb3ID_No=Label(DataFrameLeft,text="ID No.:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb3ID_No.grid(row=2,column=0,sticky="w")
textID_No=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=id_var)
textID_No.grid(row=2,column=1)

lb4FirstName=Label(DataFrameLeft,text="First Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb4FirstName.grid(row=3,column=0,sticky="w")
textFirstName=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=firstname_var)
textFirstName.grid(row=3,column=1)

lb5LastName=Label(DataFrameLeft,text="Last Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb5LastName.grid(row=4,column=0,sticky="w")
textLastName=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=lastname_var)
textLastName.grid(row=4,column=1)

lb6Address=Label(DataFrameLeft,text="Address:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb6Address.grid(row=5,column=0,sticky="w")
textAddress=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=address_var)
textAddress.grid(row=5,column=1)

lb7PostCode=Label(DataFrameLeft,text="PostCode:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb7PostCode.grid(row=6,column=0,sticky="w")
textPostCode=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=postcode_var)
textPostCode.grid(row=6,column=1)

lb7Mobile=Label(DataFrameLeft,text="Mobile No.:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb7Mobile.grid(row=7,column=0,sticky="w")
textMobile=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=mobile_var)
textMobile.grid(row=7,column=1)

lb8BookId=Label(DataFrameLeft,text="Book Id:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
lb8BookId.grid(row=8,column=0,sticky="w")
textBookId=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=bookId_var)
textBookId.grid(row=8,column=1)

lb9BookTitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb9BookTitle.grid(row=0,column=2,sticky="w")
textBookTitle=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=bookTitle_var)
textBookTitle.grid(row=0,column=3)

lb10Author=Label(DataFrameLeft,text="Author:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb10Author.grid(row=1,column=2,sticky="w")
textAuthor=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=author_var)
textAuthor.grid(row=1,column=3)

lb11DateBorrow=Label(DataFrameLeft,text="Date of Borrowed:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb11DateBorrow.grid(row=2,column=2,sticky="w")
textDateBorrow=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=dateOfBorrowed_var)
textDateBorrow.grid(row=2,column=3)

lb12DateDue=Label(DataFrameLeft,text="Date of Due:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb12DateDue.grid(row=3,column=2,sticky="w")
textDateDue=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=dateOfDue_var)
textDateDue.grid(row=3,column=3)

lb13DaysOnBook=Label(DataFrameLeft,text="Days On Book:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb13DaysOnBook.grid(row=4,column=2,sticky="w")
textDaysOnBook=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=daysOnBook_var)
textDaysOnBook.grid(row=4,column=3)

lb14LateReturnFine=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb14LateReturnFine.grid(row=5,column=2,sticky="w")
textLateReturnFine=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=lateReturnFine_var)
textLateReturnFine.grid(row=5,column=3)

lb15DateOverDue=Label(DataFrameLeft,text="Date Over Due:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb15DateOverDue.grid(row=6,column=2,sticky="w")
textDateOverDue=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=dateOverDue_var)
textDateOverDue.grid(row=6,column=3)

lb16ActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("arial",12,"bold"),padx=9,pady=4)
lb16ActualPrice.grid(row=7,column=2,sticky="w")
textActualPrice=Entry(DataFrameLeft,font=("arial",13),width=29,textvariable=actualPrice_var)
textActualPrice.grid(row=7,column=3)
        #--------------------------------------------DataFrameRight------------------------------------------------

DataFrameRight=LabelFrame(frame,text=" Book Details",bg="powder blue",fg="blue",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameRight.place(x=910,y=5,width=540,height=350)

txtBox=Text(DataFrameRight,font=("arial",12),width=32,height=15,padx=7,pady=6)
txtBox.grid(row=0,column=2)

listScrollbar=Scrollbar(DataFrameRight)
listScrollbar.grid(row=0,column=1,sticky="ns")

listBooks=["Head Python","Learn Coding","Python for Developer"]

def selectbook(evevt):
    value=str(listBox.get(ANCHOR))
    x=value
    if (x=="Head Python"):
        bookId_var.set("BKID5012")
        bookTitle_var.set("Python Organ")
        author_var.set("Charlis")

        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        dateOfBorrowed_var.set(d1)
        dateOfDue_var.set(d3)
        daysOnBook_var.set(15)
        lateReturnFine_var.set("Rs.30")
        dateOverDue_var.set("No")
        actualPrice_var.set("Rs.450")

    if (x=="Learn Coding"):
        bookId_var.set("BKID5013")
        bookTitle_var.set("Python Manual")
        author_var.set("John Adam")

        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=16)
        d3=d1+d2
        dateOfBorrowed_var.set(d1)
        dateOfDue_var.set(d3)
        daysOnBook_var.set(15)
        lateReturnFine_var.set("Rs.50")
        dateOverDue_var.set("No")
        actualPrice_var.set("Rs.345")

    if (x=="Python for Developer"):
        bookId_var.set("BKID5014")
        bookTitle_var.set("Code for Developer")
        author_var.set("Charlis")

        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        dateOfBorrowed_var.set(d1)
        dateOfDue_var.set(d3)
        daysOnBook_var.set(15)
        lateReturnFine_var.set("Rs.40")
        dateOverDue_var.set("No")
        actualPrice_var.set("Rs.400")

listBox=Listbox(DataFrameRight,font=("arial",12,),width=20,height=15)
listBox.bind("<<ListboxSelect>>",selectbook)
listBox.grid(row=0,column=0,padx=4)
listScrollbar.config(command=listBox.yview)

for item in listBooks:
    listBox.insert(END,item)

        #----------------------------------------Button Frame--------------------------------------------------------

framebutton=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
framebutton.place(x=0,y=530,width=1530,height=70)

ButtonAddData=Button(framebutton,text="Add Data",command=addadata,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonAddData.grid(row=0,column=0)

ButtonShowData=Button(framebutton,text="Show Data",command=showData,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonShowData.grid(row=0,column=1)

ButtonUpdateData=Button(framebutton,text="Update Data",command=update,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonUpdateData.grid(row=0,column=2)

ButtonDeleteData=Button(framebutton,text="Delete Data",command=delete,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonDeleteData.grid(row=0,column=3)

ButtonResetData=Button(framebutton,text="Reset Data",command=reset,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonResetData.grid(row=0,column=4)

ButtonExitData=Button(framebutton,text="Exit",command=Exit,font=("arial",12,),width=26,bg="blue",fg="white")
ButtonExitData.grid(row=0,column=5)

        #-------------------------------------Information Frame---------------------------------------------------------

framedetails=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
framedetails.place(x=0,y=600,width=1530,height=210)

Table_frame=Frame(framedetails,bd=6,relief=RIDGE,bg="powder blue")
Table_frame.place(x=0,y=2,width=1460,height=180)

xscroll=Scrollbar(Table_frame,orient=HORIZONTAL)
yscroll= Scrollbar(Table_frame,orient=VERTICAL)

Library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname","lastname","address","postcode","mobile","bookid",
                                                        "booktitle","author","dateofborrowed","dateofdue","daysonbook","latereturnfine","dateoverdue",
                                                        "actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)

xscroll.config(command=Library_table.xview)
yscroll.config(command=Library_table.yview)

Library_table.heading("membertype",text="Member Type")
Library_table.heading("prnno",text="PRN NO.")
Library_table.heading("idno",text="ID No.")
Library_table.heading("firstname",text="First Name")
Library_table.heading("lastname",text="Last Name")
Library_table.heading("address",text="Address")
Library_table.heading("postcode",text="Post Code")
Library_table.heading("mobile",text="Mobile No.")
Library_table.heading("bookid",text="Book Id")
Library_table.heading("booktitle",text="Book Title")
Library_table.heading("author",text="Author")
Library_table.heading("dateofborrowed",text="Date Of Borrowed")
Library_table.heading("dateofdue",text="Date Of Due")
Library_table.heading("daysonbook",text="Days On Book")
Library_table.heading("latereturnfine",text="Late Return Fine")
Library_table.heading("dateoverdue",text="Date Over Due")
Library_table.heading("actualprice",text="Actual Price")

Library_table["show"]="headings"
Library_table.pack(fill=BOTH,expand=1)

Library_table.column("membertype",width=100)
Library_table.column("prnno",width=100)
Library_table.column("idno",width=100)
Library_table.column("firstname",width=100)
Library_table.column("lastname",width=100)
Library_table.column("address",width=150)
Library_table.column("postcode",width=100)
Library_table.column("mobile",width=100)
Library_table.column("bookid",width=100)
Library_table.column("booktitle",width=100)
Library_table.column("author",width=100)
Library_table.column("dateofborrowed",width=150)
Library_table.column("dateofdue",width=150)
Library_table.column("daysonbook",width=100)
Library_table.column("latereturnfine",width=100)
Library_table.column("dateoverdue",width=100)
Library_table.column("actualprice",width=100)

fatch_data()
Library_table.bind("<ButtonRelease-1>",get_cursor)



    
root.mainloop()