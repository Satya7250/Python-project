'''Dictionary in Python'''

# d={100:'patna',
#    200:'delhi',
#    300:'chennai',
#    400:10+11j,10+99j:"satya",
#    0b11:'binary', #key is in int
#    'binary':0b11,
#    True:"college",
#    1:"dd", #overside, it means True==1
#    66: 10,
#    67: 10,
#    }
# print(d)
# print(type(d))


'''Empty Dictionary'''
# d={}
d=dict() #typecasting
d[100]="durga"
d[0b11]='binary'
d["satya"]='shiva'
# print(d)

# print(d[99+1])

# print(d.has_key(100))  #this object is not avaliable in python

if 100 in d:
    print(d[0b11])