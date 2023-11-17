from arrays import trig
import math
from formula import Deg,Sec,Cosec,Cot

def Trigonometry():
    t= int(input("\n\n\t\t1."+trig[1]+"  2."+trig[2]+"  3."+trig[3]+"  4."+trig[4]+"  5."+trig[5]+"  6."+trig[6]+"\n\n\t\t"))
    number = int(input("\n\n\t\tENTER NUMBER: "))
    
    if t==1:
        ans = math.cos(number)
        an = math.cos(Deg(number))
    elif t==2:
        ans = math.sin(number)
        an = math.sin(Deg(number))
    elif t==3:
        ans = math.tan(number)
        an = math.tan(Deg(number))
    elif t==4:
        ans = Sec(number)
        an = Sec(Deg(number))
    elif t==5:
        ans = Cosec(number)
        an = Cosec(Deg(number))   
    elif t==6:
        ans = Cot(number)
        an = Cot(Deg(number))
    else:
        print("\n\n\t\tINVALID CHOICE.....TRY AGAIN!!")
        
    unit= int(input("\n\n\t\t1.RADIANS  2.DEGREES  "))
    
    if unit==1:
        print("\n\n\t\tTHE "+str(trig[t])+" OF "+str(number)+" IS "+str(round(ans,4))+" IN RADIANS")
    elif unit==2:
        print("\n\n\t\tTHE "+str(trig[t])+" OF "+str(number)+" IS "+str(round(an,4))+" IN DEGREES")
    else:
        print("INVALID CHOICE....TRY AGAIN!!")
        Trigonometry()    