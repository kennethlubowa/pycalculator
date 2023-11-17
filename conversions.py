from arrays import distance,temperature,weight
from formula import Kilograms,Kilometre,Kelvin,Miles,Grams,Ounces,Pounds,Celcius,Fahreinheit,Metre

def Conversions():
    co = int(input("\n\t\t1.DISTANCE  2.WEIGHT  3.TEMPERATURE  "))
    num = float(input("\n\n\t\tENTER NUMBER: "))
    if co==1:
        d=int(input("\n\n\t\tFROM 1."+str(distance[1])+"  2."+str(distance[2])+"  3."+str(distance[3])+"  "))
        c=distance[d]
        if d==1:
            k=int(input("\n\n\tTO 2."+distance[2]+"  3."+distance[3]+"  "))
            ans=Kilometre(num,k)
        elif d==2:
            k=int(input("\n\n\tTO 1."+distance[1]+"  3."+distance[3]+"  "))
            ans=Metre(num,k)
        elif d==3:
            k=int(input("\n\n\tTO 1."+distance[1]+"  2."+distance[2]+"  "))
            ans=Miles(num,k)
        else:
            print("\n\n\t\tINVALID OPTION")
        b=distance[k]                
    elif co==2:
        d=int(input("\n\n\t\tFROM 1."+weight[1]+"  2."+weight[2]+" 3."+weight[3]+" 4."+weight[4]+"  "))
        c=weight[d]
        if d==1:
            k=int(input("\n\n\tTO 2."+weight[2]+"  3."+weight[3]+"  4."+weight[4]+"  "))
            ans=Kilograms(num,k)
        elif d==2:
            k=int(input("\n\n\tTO 1."+weight[1]+"  3."+weight[3]+"  4."+weight[4]+"  "))
            ans=Grams(num,k)
        elif d==3:
            k=int(input("\n\n\tTO 1."+weight[1]+"  2."+weight[2]+"  4."+weight[4]+"  "))
            ans=Pounds(num,k)
        elif d==4:
            k=int(input("\n\n\tTO 1."+weight[1]+"  2."+weight[2]+"  3."+weight[3]+"  "))
            ans=Ounces(num,k)    
        else:
            print("\n\n\t\tINVALID OPTION")
        b=weight[k]   
    elif co==3:
        d=int(input("\n\n\t\tFROM 1."+temperature[1]+"  2."+temperature[2]+" 3."+temperature[3]+"  "))
        c=temperature[d]
        if d==1:
            k=int(input("\n\n\tTO 2."+temperature[2]+"  3."+temperature[3]+"  "))
            ans=Celcius(num,k)
        elif d==2:
            k=int(input("\n\n\tTO 1."+temperature[1]+"  3."+temperature[3]+"  "))
            ans=Fahreinheit(num,k)
        elif d==3:
            k=int(input("\n\n\tTO 1."+temperature[1]+"  2."+temperature[2]+"  "))
            ans=Kelvin(num,k)
        else:
            print("\n\n\t\tINVALID OPTION")
        b=temperature[k]                
    else:
        print("\n\n\t\tINVALID CHOICE....TRY AGAIN!!!")
        Conversions()
    print("\n\n\t\t"+str(num)+" "+str(c)+" IS "+str(round(ans,4))+" IN "+str(b))    