# write a program in Python to create calculator using function
def sum(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
   return x/y

def takeInput():
    a= float(input("Enter the 1st value: "))
    b= float(input("Enter the 2nd value: "))
    return a,b

print("press 1 for +")
print("press 2 for -")
print("press 3 for *")
print("press 4 for /")
print("press 0 for exit")

x=1
while(x!=0):
    userInput = int(input("Enter your choice: "))
    if(userInput==0):
        print("Program is exiting...!")
        x=0
    elif(userInput==1):
        a,b=takeInput()
        print(sum(a,b))
    elif(userInput==2):
        a,b=takeInput()
        print(subtract(a,b))
    elif(userInput==3):
        a,b=takeInput()
        print(multiply(a,b))
    elif(userInput==4):
        a,b=takeInput()
        if(b!=0):
            print(divide(a,b))
        else:
            print("Divide is not possible")
            x=0
    else:
        print("invalid Choice Enter the correct input")
