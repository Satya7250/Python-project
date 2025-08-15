num=int(input("Enter the nth num: "))
a=0
b=1
i=1
print(a,",")
print(b,",")
while(i<=num):
    temp=a+b
    print(temp,",")
    a=b
    b=temp
    i+=1

