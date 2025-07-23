#to check weather the number is prime or not
num=int(input("Enter the number: "))
i=1
count=0
while(i<=num):
    if(num%i==0):
        count+=1
    i+=1
if(count==2):
    print(num,"is prime number")
else:
    print(num,"is not prime")