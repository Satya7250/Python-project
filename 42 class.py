def Avg(x, y, z):
    return (x+y+z)/3
i=1
while(i!=0):
    print("Press 1 to find average")
    print("Press 0 to exit")

    choice = int(input("Enter your choice: "))
    if (choice==0):
        print("Program is exiting...!")
        i=0
        
    elif (choice == 1):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        z = float(input("Enter third number: "))
        print("Average:",Avg(x, y, z))


# def add(x,y):
#     return x+y
# # add(x,y) # it will not work because we can not store value anywhere

# print("sum:",add(x,y))

# # z= add(x,y)
# print("sum",z)