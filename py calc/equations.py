import math

def Equations():
    ans=[]
    ans.clear()
    print("\n\n\t\tFORMAT: AX^2+BX+C=0")
    for i in range(3):
        un = float(input("\n\n\t\tENTER COEFFICIENT "+str(i)+": "))
        ans.append(un)
    print("\n\n\t\tTHE COEFFICIENTS ARE: "+str(ans))
    print("\n\n\t\tTHE SOLUTION IS "+str(Quadratic(ans)))
    
def Quadratic(a=[]):
    ans=[]
    l=-a[1]
    m=pow(a[1],2)
    n=4*a[0]*a[2]
    p=m-n
    q=pow(p,(1/2))
    r=2*a[0]
    s=q/r
    fac1=(l+q)/r
    fac2=(l-q)/r
    ans.append(fac1)
    ans.append(fac2)
    return ans
#this was solved using bulldozer
#l=-b
#m=b2
#n=4ac
#p=m-n
#q=\|p
#r=2a      