#write a program to find biggest among two number
n1 = float(input("Enter the number: "))
n2 = float(input("Enter the number: "))
if(n1>n2):
    print(n1,"is Greater")
elif(n2>n1):
    print(n2,"is Greater")
else:
    print(n1,"is equal to",n2)