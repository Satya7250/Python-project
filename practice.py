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
year = 2024
if year%4 ==0 and year%100 != 0 or year%400 == 0:
    print("leap year")
else:
    print("not leap year")