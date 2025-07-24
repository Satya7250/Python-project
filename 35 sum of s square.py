#sum of n square of nth term 
num=int(input("Enter the num: "))
i=1
result=0
while(i<=num):
    result+=i*i
    i+=1
print("sum= ",result)