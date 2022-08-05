def compoundinterest(p,r,t):
    a=p*(1+(r/100))**t
    ci=a-p
    return ci
p=int(input("enter the principal :"))
r=int(input("enter the rate of interest: "))
t=int(input("enter the time period:"))
print(compoundinterest(p,r,t))