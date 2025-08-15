#prints the corresponding weekday name
num=int(input("Enter the number: "))

if((num>7) or (num<=0)):
    print("Invalid")

if((num>=1) and (num<=7)):
    if(num==1):
        print("Monday")
    if(num==2):
        print("Tuesday")
    if(num==3):
        print("Wednesday")
    if(num==4):
        print("Thursday")
    if(num==5):
        print("Friday")
    if(num==6):
        print("Saturday")
    if(num==7):
        print("Sunday")
