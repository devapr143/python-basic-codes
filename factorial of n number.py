#many methods
#method 1

def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1 :
        return 1
    else:
        fact=1
        while (n>1):
            fact*=n
            n-=1
        return fact

# method 2
def factorials(n):
    return 1 if(n==1 or n==0) else n* factorials(n-1)

num=int(input(" enter a number :"))
print("factorial of ",num,"is",factorial(num))
print("factorial of ",num,"is",factorials(num))