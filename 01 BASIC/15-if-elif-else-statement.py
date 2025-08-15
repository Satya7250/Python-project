#find the  number is odd or even take input form user
num=int(input("Enter your number: "))
if(num>0):
    if(num%2==0):
        print(num,"is Even")
    else:
        print(num,"is Odd")
else:
    print("You Enter the invalid number")