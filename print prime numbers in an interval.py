

def prime(x,y):
    prime_list=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j ==0:
                    break
            else:
                prime_list.append(i)
    return prime_list
x=int(input("enter the lower limit:"))
y=int(input("enter the upper limit:"))
g=prime(x,y)
if len(g)==0:
    print("There are no prime number in the given range")
else:
    print("There are ",len(g), "prime  number in the given range. They are",g)