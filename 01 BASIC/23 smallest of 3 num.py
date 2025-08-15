#find the smallest among three number
n1=float(input("Enter the 1st num: "))
n2=float(input("Enter the 2nd num: "))
n3=float(input("Enter the 3rd num: "))
if(n1<n2):
    if(n1<n3):
        print(n1,"is Smallest")
    else:
        print(n3,"is Smallest")
elif(n2<n1):
    if(n2<n3):
        print(n2,"is Smallest")
    else:
        print(n3,"is Smallest")
else:
    print(n1,"==",n2,"==",n3)