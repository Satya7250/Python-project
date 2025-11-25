"""first problem"""
# age = int(input("Enter the AGE: "))
# if(0<age<=13):
#     print("child")
# elif(13<age<=19):
#     print("Teengers")
# elif(19<age<=59):
#     print("Adult")
# elif(age>59):
#     print("Senior")
# else:
#     print("Invalid")
    

'''Second problem'''

# age = 26
# day = "wednesday"
# price = 12 if age >=18 else 8
# if day == "wednesday":
#     price-=2
# print("ticket price is $:",price)


'''Third Problem'''
# score = 23
# if score > 100 or score < 0:
#     print("Invalid")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("fail")

"""fourt problem"""

# fruit = "banana"
# color = "green"
# if fruit == 'banana':
#     if color == "green":
#         print("unripe")
#     elif color == 'yellow':
#         print("Ripe")
#     elif color == 'brown':
#         print("overripe")
# else:
#     print("Information not found")

'''fifth problem'''
# weather = "sunny"
# if weather == "sunny":
#     print("go for walk")
# elif  weather == "rainy":
#     print("Tead a book")
# elif weather == "snowy":
#     print("Build a snowman")
# else:
#     print("Data not found")

'''sixth problem'''
# distance = 4
# if distance<3:
#     transport = "walk"
# elif distance <=15:
#     transport = "bike"
# elif distance >15:
#     transport = "car"
# print(transport)

'''seventh problem'''
# size = 'medium'
# extraShot = 'no'
# if extraShot == 'yes':
#     message = "Extra Short of Expresso"
# else:
#     message = "no extra short of expresso"
# print(f"you order size is {size} with {message}")

'''Eight problem'''
# year = 2024
# if year%4 ==0 and year%100 != 0 or year%400 == 0:
#     print("leap year")
# else:
#     print("not leap year")

'''Ninth problem'''
# list = [1,2,3,-4,-6]
# count=0
# for i in list:
#     if i>=1:
#         count+=1
# print(count)

'''10th Problem'''
# num = 10
# sum=0
# for i in range(1,num+1):
#     if(i%2==0):
#         sum+=i
# print(sum)

'''11th problem'''
# num = 2
# for i in range(1,11):
#     if(i==5):
#         continue
#     else:
#         print(i*num)

'''12th problem'''
# string = "satyaprakash"
# rev=""
# for i in string:
#     rev=i+rev
# print(rev)

'''13th problem'''
# string = "satyaprakash"
# for char in string:
#     if string.count(char) == 1:
#         print(char)
#         break

'''14th problem'''
# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

'''15th problem'''
# con = 1
# while con:
#     num = int(input("Enter the num: "))
#     for i in range (1,11):
#         if i == num:
#           print("number match")
#           con=0
#           break

'''16th problem'''
# num = 7
# is_prime = True
# for i in range(2,num):
#     if num%i == 0:
#         is_prime = False
#         break
# if is_prime == True:
#     print("prime")
# else:
#     print("not prime")

'''17th problem'''
# item = ["apple","banana","banana","mango"]

# unique_item = set()
# for i in item:
#     if i in unique_item:
#         print("Duplicate: ",i)
#         break
#     unique_item.add(i)

'''18th problem'''
# num = 4
# def sum(num=5):
#     return num**2
# square = sum(num)
# print(square)

'''19th problem'''
# a=10
# b=20
# def sum(a,b):
#     return a+b
# result = sum(a,b)
# print(result)

'''20th problem'''
# def multiply(a,b):
#     return a*b
# print(multiply("h",3))

'''21th problem'''
# import math
# def area_curm(radius):
#     area = (radius**2)*math.pi
#     curm = 2*math.pi*radius
#     return area,curm
# a,c = area_curm(5)
# print(a)
# print(c)

'''22th problem'''
# user = "satya"
# def greet(name="user"):
#     return "hello " + name
# print(greet(user))

'''23th problem'''
# cube = lambda x: x**3
# print(cube(3))

'''24th problem'''
# total = 0
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2,3,4,5,6,7,8,9,10))
# print(sum_all(2,3))

'''25th problem'''
# chai = "lemon chai"
# print(chai[::-1])
# print(chai[1])
# print(chai[0:5])
# print(chai[:])

# rev=""
# for i in chai:
#     rev = i+rev
# if rev == chai:
#     print("palandrom")
# else:
#     print("not palandrome")

# num_list = "0123456789"
# print(num_list[:])
# print(num_list[-5:])
# print(num_list[0:7:2])
# print(num_list[0:7:3])

# string = " Satya"
# print(string.lower())
# print(string.upper())
# print(string.strip())
# print(string.replace("S","O"))

# chai="Lemon,Satya,Monika,Satya"
# print(chai.split(", "))
# print(chai.find("Satya"))
# print(chai.count("Satya"))

'''26th Problem'''
chai_types = {'masala':"spicy","Ginger": "zesty","Green": "Fresh"}
# for chai in chai_types:
#     print(chai,chai_types[chai])

# for key,value in chai_types.items():
#     print(key,value)

# chai_types['Earl Grey']= 'Citrus'
# print(chai_types)
# print(chai_types.pop('Green'))

# del chai_types['Green']
# print(chai_types)

# chai_types_copy = chai_types.copy()
# print(chai_types_copy)


# tea_shop ={
#     "chai":{"Masala":"spicy","Green":"Zesty"},
#     "name":{100:"Satya","200":"Prakash"}
# }

# print(tea_shop['chai']['Green'])

# squared_num = {x:x**2 for x in range(1,6)}
# print(squared_num)


# keys = ["Masala","Ginger","Lemon"]
# default_value = "Delicious"
# new_dict = dict.fromkeys(keys,default_value)
# print(new_dict)

'''27th problem'''
tea_types = ('black','green','oolang')
new = (1,2,3,4)
all_item = tea_types+new
print(all_item)