
n=int(input("Enter the number :"))
d=n
x=len(str(n))
sum=0
while n!=0:
    z=n%10
    sum=sum+(z**x)
    n=n//10
if d==sum:
    print("The number ",d,"is an armstrong number")
else:
    print("The number ", d, "is not an armstrong number")