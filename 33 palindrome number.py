#check the given number is palindrome or not
num=int(input("Enter the number: "))
org=num
rev=0
while(num!=0):
    if(num):
      r=num%10
      rev=rev*10+r
      num=num//10
if(org==rev):
   print(org,"is palindrome")
else:
   print(org,"is not palindrome")