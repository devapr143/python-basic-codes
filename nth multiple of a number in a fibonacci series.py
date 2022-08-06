def position(x,y):
    f1=0
    f2=1
    i=2
    while i!=0:
        f3=f1+f2
        f1=f2
        f2=f3
        if f2%x==0:
            return y*i
        i+=1
    return
y=int(input("enter multiple no. :"))
x=int(input("number whose position we are finding:"))
print("position of the multiple in fibonacci series is ",position(x,y))
