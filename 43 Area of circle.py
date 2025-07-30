# with return type
def AreaCircle(r): 
    return 3.14*r*r
    # print("Area of circle:",3.14*r*r)

print("Press 1 for continue: ")
print("Press 0 for Exit")
i=1
while(i!=0):
    choice = input("Enter choice: ")
    if (choice=="0"):
        print("Program is exiting...!")
        i=0
    elif (choice == "1"):
        radius = float(input("Enter radius: "))
        print("Area of Circle:",AreaCircle(radius))
        # AreaCircle(radius)
    else:
        print("Invalid choice. Enter again: ")