def simpleInterest(x,y,z): 
    return (x*y*z)/100

print("Press 1 for continue: ")
print("Press 0 for Exit")
i=1
while(i!=0):
    choice = input("Enter choice: ")
    if (choice=="0"):
        print("Program is exiting...!")
        i=0
    elif (choice == "1"):
        p = float(input("Enter principal: "))
        r = float(input("Enter rate: "))
        t = float(input("Enter time: "))
        print("Simple Interest:",simpleInterest(p,r,t))
    else:
        print("Invalid choice. Enter again: ")



# def simpleInterest(): 
#      p = float(input("Enter principal: "))
#      r = float(input("Enter rate: "))
#      t = float(input("Enter time: "))
#      print("Simple Interest:",(p*t*r)/100)

# print("Press 1 for continue: ")
# print("Press 0 for Exit")
# i=1
# while(i!=0):
#     choice = input("Enter choice: ")
#     if (choice=="0"):
#         print("Program is exiting...!")
#         i=0
#     elif (choice == "1"):
#         simpleInterest()
#     else:
#         print("Invalid choice. Enter again: ")