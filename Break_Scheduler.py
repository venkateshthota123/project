import time
import webbrowser
type_break=input("enter the dtype of break M for minutes H for hours")
breaks=int(input("enter the no of breaks"))
t=int(input("enter no of minutes or hours after the break"))
z=input("enter the youtube link")

for i in range(breaks):

    if type_break.lower()=='m':
        time.sleep(t*60)
        webbrowser.open(z,new=2)
    else:
        time.sleep(t*60*60)
        webbrowser.open(z,new=2)
