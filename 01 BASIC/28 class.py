# print("Welcome", end=" $")
# print("Press 1 for +")
# print("press 2 for -")
# print("press 3 for *")
# num=int(input("Enter your choice: "))
# if(num==1):
#     a=float(input("Enter the num: "))
#     b=float(input("Enter the 2nd num: "))
#     print("sum: ",a+b)
# elif(num==2):
#     a=float(input("Enter the num: "))
#     b=float(input("Enter the 2nd num: "))
#     print("subtract: ",a-b)
# elif(num==2):
#     a=float(input("Enter the num: "))
#     b=float(input("Enter the 2nd num: "))
#     print("Multiply: ",a*b)

# i = 10
# while i >= 1:
#     print(i,end=",")
#     i -=1

# num=int(input("Enter the number: "))
# i=1
# while(i<=10):
#     s=num*i
#     print(s)
#     i+=1

# num=int(input("Enter the num: "))
# sum=0
# i=1
# while(i<=num):
#     sum+=i
#     i+=1
# print(sum)

j = int(input("Enter the start: "))
k = int(input("Enter the end: "))
while (j <= k):
    if (j % 2 == 0):
        print("Even: ",j)
    elif (j % 2 != 0):
        print("Odd: ",j)
    j += 1
    
