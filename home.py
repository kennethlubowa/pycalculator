from arrays import math
from arithmetics import Arithmetics
from calculus import Calculus
from conversions import Conversions
from equations import Equations
from triginometry import Trigonometry

print("\n\n\n\n")

print("\t\tWELCOME TO MY CALCULATOR")

for i in range(50):
    count=i
    try:
        print("\n\n\n")
        print("\n\n\t1."+math[1]+"  2."+math[2]+"  3."+math[3]+"  4."+math[4]+"  5."+math[5])
        mathe = int(input("\n\n\tSELECT MATHEMATICS TO PERFORM: "))
        if mathe == 1:
            print("\n\n\tYOU CHOSE ARITHMETICS")
            Arithmetics()
        elif mathe == 2:
            print("\n\n\tYOU CHOSE TRIGONOMETRY")
            Trigonometry()
        elif mathe == 3:
            print("\n\n\tYOU CHOSE CALCULUS")
            Calculus()
        elif mathe == 4:
            print("\n\n\tYOU CHOSE QUADRATIC EQUATIONS")
            Equations()
        elif mathe == 5:
            print("\n\n\tYOU CHOSE CONVERSIONS")
            Conversions()
        else: 
            print("\n\n\tINVALID CHOICE....TRY AGAIN!!")                   
        
        choice = int(input("\n\n\t\tENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO ABORT: "))
        if choice!=1:
            break
        
    except ValueError:
        print("\n\n\t\tYOU ARE REQUIRED TO ENTER AN INTEGER NUMBER PLEASE...YOU HAVE "+str(3-i)+" CHANCE(S) LEFT...TRY AGAIN!!!")
        if count==3:
            print("\n\n\t\tCHANCES USED UP....START AFRESH!!")
            break  
        
print("\n\n\n\n")