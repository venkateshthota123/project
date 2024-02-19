import random 
import string 
from tkinter import *
from tkinter import messagebox
import pyperclip



def password():
    length=int(e1.get())
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special_charcter="~!@#$%^&*()_+{}:\"<>?`-=[];\',./=\\"
    password=upper+lower+digits+special_charcter
    password="".join(random.choices(password,k=length))
    password=list(password)
    random.shuffle(password)
    password_gen="".join(password)
    messagebox.showinfo("Result",f'your random password : {password_gen}')
    pyperclip.copy(password_gen)



base=Tk()
base.geometry("250x200")
base.title("Password generator")
e1=StringVar()
Label(base,text= "Enter the length of password").pack()
Entry(base,textvariable = e1).pack()
Button(base, text="Generate Password",command=password,height=1,width=15).pack()
base.mainloop()
