#print the number odd or even
num = int(input("Enter the number: "))
if(num>0):
    if(num%2==0):
        print(num,"is Even")
    if(num%2!=0):
        print(num,"is Odd")
if(num<=0):
    print(num,"is inValid")