from arrays import arith
from formula import Product
import math

def Arithmetics():
    lis =[]
    print("\n\t1."+arith[1]+"  2."+arith[2]+"  3."+arith[3]+"  4."+arith[4]+"  5."+arith[5])
    ar = int(input("\n\n\tENTER CHOICE: "))
    if ar==1:
        rang = int(input("\n\n\tHOW MANY NUMBERS: "))
        for k in range(rang):
            ni = float(input("\n\n\t\tENTER NUMBER: "))
            lis.append(ni)
        print("\n\t\tTHE SUM OF "+str(lis)+" IS "+str(sum(lis)))
    elif ar==2:
        first = float(input("\n\n\t\tFIRST NUMBER: "))
        second = float(input("\n\n\t\tSECOND NUMBER: "))
        print("\n\t\t"+str(first)+" - "+str(second)+" = "+str(first-second))   
    elif ar==3:
        rang = int(input("\n\n\tHOW MANY NUMBERS: "))
        for k in range(rang):
            ni = float(input("\n\n\t\tENTER NUMBER: "))
            lis.append(ni)
        print("\n\n\t\tTHE PRODUCT OF "+str(lis)+" IS "+str(Product(lis))) 
    elif ar==4:
        first = float(input("\n\n\t\tFIRST NUMBER: "))
        second = float(input("\n\n\t\tSECOND NUMBER: "))
        print("\n\n\t\t"+str(first)+" / "+str(second)+" = "+str(first/second))  
    elif ar==5:
        first = float(input("\n\n\t\tNUMBER: "))
        second = float(input("\n\n\t\tMODULE: "))
        print("\n\n\t\t"+str(first)+" % "+str(second)+" = "+str(first%second))    
    else:
        print("\n\n\t\t\tINVALID CHOICE.....TRY AGAIN!!")  
        Arithmetics()              