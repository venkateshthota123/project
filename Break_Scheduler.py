import time
import webbrowser
from tkinter import *

def  open_website():
    type_break=d1.get()
    breaks=int(d2.get())
    t=int(d3.get())
    z=d4.get()
    for i in range(breaks):

        if type_break.lower()=='m':
            time.sleep(t*60)
            webbrowser.open(z,new=2)
        else:
            time.sleep(t*60*60)
            webbrowser.open(z,new=2)

base=Tk()
base.geometry("400x300")
base.title("time schedual")

d1=StringVar()
d2=StringVar()
d3=StringVar()
d4=StringVar()

Label(base,text="enter the dtype of break M for minutes H for hours").pack(pady=10)
Entry(base,textvariable=d1).pack()
Label(base,text="Enter No Of Breaks").pack()
Entry(base,textvariable=d2).pack()
Label(base,text="Enter Minutes Or Hours After for the Break eg 30 for minutes or 2 for hours ").pack()
Entry(base,textvariable=d3).pack()
Label(base,text="enter the required link").pack()
Entry(base,textvariable=d4).pack()
Button(base,text="submit",command=open_website,height=1,width=5).pack(pady=10)



base.mainloop()
