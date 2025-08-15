a = 10
def f1():
    global b
    b=8
    print("a = ", a)
def f2():
    a=20
    print("a = ",a)
f1()
print("b: ",b) #it should print after calling a function
f2()