#print corresponding month name
num=int(input("Enter the number (1-12): "))
if(1 <= num <= 12):
    if(num==1):
        print("January")
    elif(num==2):
        print("February")
    elif(num==3):
        print("March")
    elif(num==4):
        print("April")
    elif(num==5):
        print("May")
    elif(num==6):
        print("June")
    elif(num==7):
        print("July")
    elif(num==8):
        print("August")
    elif(num==9):
        print("September")
    elif(num==10):
        print("October")
    elif(num==11):
        print("November")
    else:
        print("December")
else:
    print("You Enter Invalid number")
    
