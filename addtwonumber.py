if __name__ =="__main__" :
  num1=float(input("enter a number : "))
  num2 = float(input("enter another number : "))
  sumof= lambda  num1, num2 :num1+num2
  print("sum of {} and {} is {} ".format(num1,num2,sumof(num1,num2)))