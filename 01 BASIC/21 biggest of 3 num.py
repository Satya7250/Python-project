#write a program to find greatest among 3 number
n1=float(input("Enter the 1st num: "))
n2=float(input("Enter the 2nd num: "))
n3=float(input("Enter the 3rd num: "))
if(n1>n2):
    if(n1>n3):
        print(n1,"is Greater")
    else:
        print(n3,"is Greater")
elif(n1<n2):
    if(n2>n3):
        print(n2,"is Greater")
    else:
        print(n3,"is Greater")
else:
    print(n1,"==",n2,"==",n3)