#write a program to check that num is divisible by 7 and 3 or not
num=int(input("Enter the number: "))
if((num%7==0) and (num%3==0)):
    print(num,"Divisible by both 3 and 7")
elif(num%7==0):
    print(num,"Divisible by 7")
elif(num%3==0):
    print(num,"Divisible by 3")
else:
    print("Not Divisible by 7 and 3")