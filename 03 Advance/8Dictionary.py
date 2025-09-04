# d = {
#     3:"apple",
#     4:[8888,3,"tt",]
# }
# print(d)
# print(len(d))
# d.clear()
# del(d)

# print(d.get(43)) #none
# print(d.get(3)) #apple

# print(d.get(5,100))
# print(d.pop(3))

# d.popitem() #it remove random key value pair

# print(d.keys()) #it return all keys only
# print(d.values()) #it return all value only
# print(d.items()) #it return complete dictionary
# d1 = d.copy() #copy the dictionary
# print(id(d1))
# print(id(d))

# print(d.setdefault(3,555)) #if value exit it return else return default vlaue

# d=eval(input("Enter the num: "))
# s=sum(d.values())
# print("sum: ",s)

# word = input("Enter any word: ")
# d={}
# for x in word:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,"occurred",v,"times")

'''for x in word:
    d[x]=d.get(x,0)+1
print(d)'''


