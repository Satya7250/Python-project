#Aliasing in function
# def subtract(a,b):
#     return a-b
# s = subtract
# print("subtract: ",s(20,10))





# def add(a,b): #parameter
#     sum = a+b
#     sub = a-b
#     product = a*b
#     return sum,sub,product
# x,y,z = add(3,5) #argument
# print("sum: ",x)
# print("subtraction: ",y)
# print("Product: ",z)




# def sum(a,b):
#     result = a-b
#     return result
# print("The subtraction result: ", sum(a=10,b=9)) #1
# print("The subtraction result: ", sum(b=9,a=10)) #1
# print("The subtraction result: ", sum(10,9)) #1
# print("The subtraction result: ", sum(9,10)) #-1
# print("The subtraction result: ", sum(10,9,8)) #it show error
# print("The subtraction result: ", sum(10)) #it show error due to less actual argument


#default arguments
# def sub(a=100,b=10,c=10):
#     res = a-b-c
#     return res
# print("The subtraction result: ",sub())
# print("The subtraction: ", sub(5,5))
# print("The subtraction: ",sub(2,4,5,5))#it show error more number of arguments





#variable length argument

def sum(*n): #variable length argument
    total = 0
    for n1 in n: 
        total = total + n1
    print("The sum: ", total)

sum()# function call
sum(10, 30) # two actual argumet passed in function call
sum(10, 10, 20, 10, 20)
