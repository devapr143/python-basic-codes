import math
def perfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def fibonacci(n):
    return perfectsquare(5*n*n+4)or perfectsquare(5*n*n-4)
z=int(input("enter lower limit:"))
y=int(input("enter upper limit:"))
for i in range (z,y):
    if fibonacci(i)== True:
        print(i,"is a fibonacci number")
    else:
        print(i,"is not a fibonacci number")