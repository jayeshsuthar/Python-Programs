def factorial(x):
    if  x==1:
        return 1
    else:
        return x * factorial(x-1)

fact = 1
def fact(x):
    while x>0:
        fact = fact * x
        x=-1

x = int(input("Enter Number "))
print("factorial of ", x ,"  is ",fact(x))
