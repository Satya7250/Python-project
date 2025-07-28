#using function write a program in python to display mathematical table

userNum = int(input("Enter the number: "))

def showTable(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
showTable(userNum)