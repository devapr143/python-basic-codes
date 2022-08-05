def areacircle(r):
    pi=3.142
    return pi*(r**2)
def areasqaure(a):
    return a**2
def arearectangle(l,b):
    return l*b
x=int(input("enter 1 for circle,2 for sqaure, 3 for rectangle:"))
if x==1:
    r=int(input("enter radius of the circle:"))
    print(areacircle(r))
elif x==2:
    a=int(input("enter the length of a side of square:"))
    print(areasqaure(a))
elif x==3:
    l=int(input("enter the value of a longer side :"))
    b=int(input("enter the value of smaller side :"))
    print(arearectangle(l,b))
else:
    print("The option you have selected is incorrect please try again")
