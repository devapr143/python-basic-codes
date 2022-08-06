def exposum(n,p,g):
    sm=0
    for i in range(n,p+1):
        sm=sm+pow(i,g)
    return sm
n=int(input("enter the lower limit :"))
p=int(input("enter the upper limit :"))
g=int(input("enter the exponential power"))
print(exposum(n,p,g))