
def exposum(n,g):
    sm=0
    for i in range(1,n+1):
        sm=sm+pow(i,g)
    return sm
f=int(input("enter the number of natural number:"))
g=int(input("enter the exponent for the sum:"))
print(exposum(f,g))