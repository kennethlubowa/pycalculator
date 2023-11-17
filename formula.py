import math
kelvin=273.15
mile=1609.344
ounce=28.25
pound=453.592

def Product(a=[]):
    ans = 1
    for i in range(len(a)):
        ans = ans*a[i]
    return ans

def Log(a,b):
    ans = math.log(a)/math.log(b)
    return ans

def Root(a,b):
    ans = math.pow(a,(1/b))
    return ans

def Cot(n):
    return math.cos(n)/math.sin(n)

def Cosec(n):
    return 1/math.sin(n)

def Sec(n):
    return 1/math.cos(n)

def Deg(n): #converting from radians to degrees
    ans=((n*math.pi)/180)
    return ans

def Multiples(a=[]):
    ans =[{""}]
    ans.clear()
    com={""}
    com.clear()
    lim = int(input("\n\n\t\tENTER LIMIT: "))
    for i in range(len(a)):
        mul ={""}
        mul.clear()
        mul.add(a[i])
        z=a[i]+a[i]
        mul.add(z)
        while(z<=lim):
            z=z+a[i]
            if(not(z>lim)):
                mul.add(z)
        print("\n\n\t\tMULTIPLES OF "+str(a[i])+" NOT EXCEEDING "+str(lim)+" ARE "+str(mul))     
        ans.append(mul)
    ref=ans[0]
    for h in range(0,len(ans)):
        reflist=ans[h]
        com=ref.intersection(reflist)
        ref=com   
    print("\n\n\t\tTHE COMMON MULTIPLES ARE "+str(ref))    
    return ref
        
def Factors(a=[]):
    ans = [{""}]
    ans.clear()
    com={""}
    com.clear()
    for i in range(len(a)):
        fact={""}
        fact.clear()
        for j in range(1,int(a[i])):
            if a[i]%j==0:
                fact.add(j)
        fact.add(a[i])
        print("\n\n\t\tFACTORS OF "+str(a[i])+" ARE "+str(fact))
        ans.append(fact) 
    ref = ans[0] 
    ans.remove(ref)   
    for n in ans:
        com = ref.intersection(n)
    print("\n\n\t\tTHE COMMON FACTORS ARE "+str(com))    
    return com

def Kilometre(n,a):
    if a==2: #to metres
        ans=n*1000
    else: #to miles
        ans=1000*(n/mile)
    return ans        
    
def Metre(n,a):
    if a==1: #to kilometres
        ans=n/1000
    else: #to miles
        ans=n/mile
    return ans     

def Miles(n,a):
    if a==2: #to metres
        ans=n*mile
    else: #to kilometres
        ans=(n*mile)/1000
    return ans     

def Kilograms(n,a):
    if a==2: #to grams
        ans=n*1000
    elif a==3: #to pounds
        ans=(n*1000)/pound    
    else: #to ounces
        ans=(n*1000)/ounce
    return ans     

def Grams(n,a):
    if a==3: #to pounds
        ans=n/pound
    elif a==4: #to ounces
        ans=n/ounce    
    else: #to kilometres
        ans=(n/1000)
    return ans     

def Pounds(n,a):
    if a==2: #to grams
        ans=n*pound
    elif a==4: #to ounces
        ans=n*pound*ounce    
    else: #to kilograms
        ans=(n*pound)/1000
    return ans     

def Ounces(n,a):
    if a==1: #to kilograms
        ans=(n*ounce)/1000
    elif a==2: #to grams
        ans=n*ounce    
    else: #to pounds
        ans=n*ounce*pound
    return ans    

def Celcius(n,a):
    if a==2: #to fahreinheit
        ans=(n*(9/5)+32)
    else: #to kelvin
        ans=n+kelvin
    return ans     

def Fahreinheit(n,a):
    if a==1: #to celcius
        ans=((n-32)*(5/9))
    else: #to kelvin
        ans=(kelvin+((n-32)*(5/9))) 
    return ans    

def Kelvin(n,a):
    if a==1: #to celcius
        ans=n-kelvin
    else: #to fahreinheit
        c=n-kelvin
        ans=((c*(9/5)),32)
    return ans         