#print the corrosponding weekname
num=int(input("Enter the number: "))
if(1 <= num <= 7):
    if(num==1):
        print("Monday")
    elif(num==2):
        print("Tuesday")
    elif(num==3):
        print("Wednesday")
    elif(num==4):
        print("Thursday")
    elif(num==5):
        print("Friday")
    elif(num==6):
        print("Saturday")
    elif(num==7):
        print("Sunday")
else:
    print("Invalid")