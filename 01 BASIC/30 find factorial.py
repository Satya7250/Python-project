#write a program to find the factorial of a number
num=int(input("Enter the number to find fact: "))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print("Factorial is: ",fact)