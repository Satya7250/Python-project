#find the smallest among two number
n1=float(input("Enter the number: "))
n2=float(input("Enter the 2nd num: "))
if(n1>n2):
    print(n2,"is Smallest")
elif(n2>n1):
    print(n1,"is Smallest")
else:
    print(n1,"is equal to",n2)