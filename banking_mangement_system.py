from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Venky@057",
      database="banking_system"
)
mycursor = mydb.cursor()

def createnewaccount():
    root = Toplevel()
    root.title("Create new account")
    root.geometry("200x200")
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    Label(root, text='Name').grid(row=0, column=1)
    Entry(root, textvariable=s1).grid(row=0, column=2)
    Label(root, text='Accountnumber').grid(row=1, column=1)
    Entry(root, textvariable=s2).grid(row=1, column=2)
    Label(root, text='account_balance').grid(row=3, column=1)
    Entry(root, textvariable=s3).grid(row=3, column=2)
    def submit(name, account_number, account_balance):
        try:
            sql = "INSERT INTO banking (name, account_number, account_balance) VALUES (%s, %s, %s)"
            value = (name, account_number, account_balance)
            mycursor.execute(sql, value)
            mydb.commit()
            messagebox.showinfo("Result", "Data entered successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    Button(root, text="submit", command=lambda: submit(s1.get(), s2.get(), s3.get())).grid(row=4, column=1)
    root.mainloop()



def checkbalance():
    root1 = Toplevel()
    root1.title("Check balance")
    root1.geometry("200x200")
    n1 = StringVar()
    Label(root1, text="enter account number").grid(row=0, column=1)
    Entry(root1, textvariable=n1).grid(row=1, column=1)
    def submit1():
        e4 = n1.get()
        try:
            sql = "SELECT account_balance FROM banking WHERE account_number=%s"
            val = (e4,)
            mycursor.execute(sql, val)
            res = mycursor.fetchone()
            if res:
                messagebox.showinfo("Result", f"Account balance: {res[0]}")
            else:
                messagebox.showinfo("Result", "Account not found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    Button(root1, text="submit", command=submit1).grid(row=2, column=2)
    root1.mainloop()


        
def withdraw():
    root2 = Toplevel()
    root2.title("Withdraw")
    root2.geometry("200x200")
    n2 = StringVar()
    required_money = StringVar()
    Label(root2, text="enter the account number").grid(row=0, column=1)
    Entry(root2, textvariable=n2).grid(row=1, column=1)
    Label(root2, text="enter the required money").grid(row=2, column=1)
    Entry(root2, textvariable=required_money).grid(row=3, column=1)
    
    def submit_withdraw():
        account_number = n2.get()
        required_money_value = required_money.get()
        my_balance_query = "SELECT account_balance FROM banking WHERE account_number=%s"
        val = (account_number,)
        mycursor.execute(my_balance_query, val)
        res = mycursor.fetchone()
        if res:
            present_money = res[0]
            if int(present_money) >= int(required_money_value):
                remaining_money = int(present_money) - int(required_money_value)
                remaining_money = str(remaining_money)
                update_balance_query = "UPDATE banking SET account_balance=%s WHERE account_number=%s"
                value = (remaining_money, account_number)
                mycursor.execute(update_balance_query, value)
                mydb.commit()
                messagebox.showinfo("Withdraw", "Withdraw successful")
            else:
                messagebox.showinfo("Withdraw", "Insufficient balance")
        else:
            messagebox.showinfo("Withdraw", "Account not found")
    
    Button(root2, text="Submit", command=submit_withdraw).grid(row=4, column=1)
    root2.mainloop()

def add_money():
    root3=Toplevel()
    root3.title("Adding_Money")
    root3.geometry("200x200")
    accountnumber=StringVar()
    amount=StringVar()
    Label(root3,text="enter the account number").grid(row=0,column=1)
    Entry(root3,textvariable=accountnumber).grid(row=1,column=1)
    Label(root3,text="enter the amount").grid(row=2,column=1)
    Entry(root3,textvariable=amount).grid(row=3,column=1)
    
    def submit3():
        account_number=accountnumber.get()
        money=amount.get()
        if len(money)=='0':
            messagebox.showinfo("add_money","enter value correctly")
        else:
            sql="SELECT account_balance from banking where account_number=%s"
            value=(account_number,)
            mycursor.execute(sql,value)
            res=mycursor.fetchone()
            result=int(res[0])+int(money)
            result=str(result)
            query="UPDATE  banking SET account_balance=%s WHERE account_number=%s"
            val=(result,account_number)
            mycursor.execute(query,val)
            mydb.commit()
            messagebox.showinfo("add_money","Money added successfully ")
    Button(root3,text="submit",command=submit3).grid(row=4,column=1)
    root3.mainloop()

def deleteaccount():
    root4=Toplevel()
    root4.title("Deleting account")
    root4.geometry("200x200")
    d1=StringVar()
    Label(root4,text="Enter the account number").grid(row=0,column=1)
    Entry(root4,textvariable=d1).grid(row=1,column=1)
    def submit4():
        n1=d1.get()
        sql="SELECT * FROM banking WHERE account_number=%s"
        val=(n1,)
        mycursor.execute(sql,val)
        res=mycursor.fetchone()
        if res:
            q="DELETE FROM banking WHERE account_number=%s"
            mycursor.execute(q,val)
            mydb.commit()
            messagebox.showinfo("delete account","account deleted")
        else:
            messagebox.showinfo("delete account","no account")
    Button(root4,text="submit",command=submit4).grid(row=4,column=1)
    root4.mainloop()
            
def transfer_money():
    root5=Toplevel()
    root5.title("money_transfer")
    root5.geometry("200x200")
    g1=StringVar()
    g2=StringVar()
    g3=StringVar()
    Label(root5,text="Enter your bank account number").grid(row=0,column=1)
    Entry(root5,textvariable=g1).grid(row=1,column=1)
    Label(root5,text="Enter your bank trensfer account number").grid(row=2,column=1)
    Entry(root5,textvariable=g2).grid(row=3,column=1)
    Label(root5,text="Enter amount to transfer ").grid(row=4,column=1)
    Entry(root5,textvariable=g3).grid(row=5,column=1)
    def submit5():
        ac1=g1.get()
        ac2=g2.get()
        mon=g3.get()
        sql1="SELECT * FROM banking WHERE account_number=%s"
        val1=(ac1,)
        mycursor.execute(sql1,val1)
        res1=mycursor.fetchone()
        sql2="SELECT * FROM banking WHERE account_number=%s"
        val2=(ac2,)
        mycursor.execute(sql2,val2)
        res2=mycursor.fetchone()
        if res1 and res2:
            if int(res1[2])>=int(mon):
                transfering_money=int(res1[2])-int(mon)
                transferd_money=int(res2[2])+int(mon)
                sql1="UPDATE banking SET account_balance=%s where account_number=%s"
                val1=(str(transfering_money),ac1)
                mycursor.execute(sql1,val1)
                mydb.commit()
                sql2="UPDATE banking SET account_balance=%s where account_number=%s"
                val2=(str(transferd_money),ac2)
                mycursor.execute(sql2,val2)
                mydb.commit()
                messagebox.showinfo("transfer money","money transferd successful") 
            else:
                messagebox.showinfo("transfer money","insufficient balance")
            
        else:
            messagebox.showinfo("transfer money","one of the account is not present in our bank")
        
    Button(root5,text="submit",command=submit5).grid(row=6,column=1)
    root5.mainloop()
            
        
def submit_all():
    try:
        sql="SELECT * FROM banking"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        l=[]
        for i in res:
            l.append(i)
        print(l)
        for j in l:
            messagebox.showinfo("data",f"name:{j[0]} \n account_number:{j[1]} \n account_balance:{j[2]}")
    except Exception as e:
        messagebox.showerror("Error"," no details")

base = Tk()
base.title("Banking system")
base.geometry("300x300")

Button(base, text="create account", command=createnewaccount, bg='green', fg='white', width=30, height=2).pack()
Button(base, text="check balance", command=checkbalance, bg='blue', fg='orange', width=30, height=2).pack()
Button(base,text="withdraw",command=withdraw,bg='yellow',fg='red',width=30,height=2).pack()
Button(base,text="add money",command=add_money,bg='green',fg='blue',width=30,height=2).pack()
Button(base,text="money transfer ",command=transfer_money,bg='purple',fg='white',width=30,height=2).pack()
Button(base,text="delete account",command=deleteaccount,bg='red',fg='white',width=30,height=2).pack()
Button(base,text="all details",command=submit_all,bg='orange',fg='white',width=30,height=2).pack()

base.mainloop()
