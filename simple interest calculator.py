def simpleinterest(p,t,r):
    print("the principal is", p)
    print("the time period is",t )
    print("the rate of interest is", r)
    interest=(p*t*r)/100
    print(" The simple interest is", interest)
p = float(input("enter principal :"))
t=float(input("enter time period :"))
r=float(input("enter rate of interest :"))
simpleinterest(p,t,r)
