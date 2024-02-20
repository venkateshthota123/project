from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Venky@057",
        database="job"
    )
mycursor=mydb.cursor()
#mycursor.execute("create table student_name (name varchar(25),phone varchar(10),email varchar(50),address varchar(256))")  # already used so give error commented

def submit():
    e1=name.get()
    e2=phone.get()
    e3=email.get()
    e4=address.get()
    mycursor=mydb.cursor()
    sql="INSERT INTO student_name (name,phone,email,address) values (%s,%s,%s,%s) "
    value=(e1,e2,e3,e4)
    mycursor.execute(sql,value)
    mydb.commit()
    messagebox.showinfo('Success','Data Submitted Successfully')

def data():
    mycursor=mydb.cursor()
    mycursor.execute("select * from student_name")
    row=mycursor.fetchall()
    list_1=[]
    for i in row:
        list_1.append(i)
    messagebox.showinfo('Result',list_1)
        



base=Tk()
base.title("google form")
base.geometry("400x350")

name=StringVar()
Label(base,text= "Enter Full Name:").grid(row=0,column=1)
Entry(base,textvariable=name).grid(row=0, column=2)

phone=StringVar()
Label(base, text="Phone Number:").grid(row=1, column=1)
Entry(base,textvariable=phone).grid(row=1, column=2)

email=StringVar()
Label(base,text="Email ID:").grid(row=2,column=1)
Entry(base,textvariable=email).grid(row=2, column=2)

address=StringVar()
Label(base, text="Address:").grid(row=3, column=1)
Entry(base, textvariable=address,width=30).grid(row=3, column=2)

Button(base,text= "Submit", command=submit, bg='green', fg='white').grid(row=4, columnspan=2)

Button(base,text='show data',command=data,bg='yellow').grid(row=4,columnspan=3)

base.mainloop()
