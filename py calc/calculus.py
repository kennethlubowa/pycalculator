from arrays import calc
from formula import Log,Root,Multiples,Factors
import math

def Calculus():
    print("\n\t1. "+calc[1]+"  2. "+calc[2]+"  3. "+calc[3])
    ca = int(input("\n\n\tSELECT CALCULUS KIND: "))
    
    if ca==1:
        num = float(input("\n\n\t\tENTER NUMBER: "))
        print("\n\n\t1.NATURAL LOGARITHM  2.SPECIFIC BASE")
        og = int(input("\n\n\tSELECT LOGARITHM KIND: "))
        if og==1:
            print("\n\n\t\tTHE NATURAL LOGARITHM OF "+str(num)+" IS "+str(math.log(num)))
        elif og==2:
            b = float(input("\n\n\t\tENTER BASE: "))
            print("\n\n\t\tTHE LOGARITHM OF "+str(num)+" TO BASE "+str(b)+" IS "+str(Log(num,b))) 
        else:
            print("\n\n\t\tINVALID CHOICE...TRY AGAIN")       
    elif ca==2: 
        num = float(input("\n\n\t\tENTER NUMBER: "))
        print("\n\n\t1.SQUARE ROOT  2.CUBE ROOT  3.SPECIFIC ROOT")
        ro = int(input("\n\n\tSELECT WHICH ROOT: "))
        if ro==1:
            print("\n\n\tTHE SQUARE ROOT OF "+str(num)+" IS "+str(math.sqrt(num)))
        elif ro==2:
            print("\n\n\tTHE CUBE ROOT OF "+str(num)+" IS "+str(Root(num,3)))    
        elif ro==3:
            ot = float(input("\n\n\t\tENTER ROOT: "))
            print("\n\n\tTHE "+str(ot)+"th ROOT OF "+str(num)+" IS "+str(Root(num,ot))) 
        else:
            print("\n\n\t\tINVALID CHOICE... TRY AGAIN!!!")      
    elif ca==3:
        a=[]
        n = int(input("\n\n\t\tHOW MANY NUMBERS: "))
        for z in range(n):
            um = float(input("\n\n\t\tENTER NUMBER: "))
            a.append(um)
        f = int(input("\n\n\t\t1.LCM  2.GCF   "))  
        if f==1:
            mult=[]
            mult.clear()
            try:
                mults = Multiples(a)    
                for z in mults:
                    mult.append(z)
                    mult.sort()
                print("\n\n\t\tTHE LCM OF "+str(a)+" IS "+str(mult[0]))    
            except IndexError:
                print("\n\n\t\t"+str(a)+" HAVE NO COMMON MULTIPLES")
        
        elif f==2:
            fact=[]
            fact.clear()
            facts = Factors(a)
            for z in facts:
                fact.append(z)
            fact.sort()
            fact.reverse()
            print("\n\n\t\tTHE GCF OF "+str(a)+" IS "+str(fact[0]))    
        else:
            print("\n\n\tINVALID CHOICE...TRY AGAIN!!!")    
    else:
        print("\n\n\t\tINVALID CHOICE.... TRY AGAIN!!!")
        Calculus()    