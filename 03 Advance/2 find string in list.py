# user_list = eval(input("Enter a list: "))
# if "katihar" in user_list:
#     print("katihar exists in the list.")
# else:
#     print("katihar does not exist in the list.")



# user_list = eval(input("Enter a list: "))
user_list = input("Enter a list:").split(" ")
print("user_list: ", user_list)
found = 0
for item in user_list:
    if item == "katihar":
        found = 1
if found:
    print("katihar exists in the list.")
else:
    print("katihar does not exist in the list.")