class student:
    '''this class developed by satyaPrakash'''
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Helllo My name is:", self.name)
        print("my rollno is:",self.rollno)
        print("my Marks are: ", self.marks)

s1 = student("Durga",108,80)
s2 = student("Satya",109,8)
# s2.talk()
# s1.talk()


# print(student.__doc__)
# help(student)


class test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = test()
t.m1()
print(t.__dict__)
