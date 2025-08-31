intNum = 10
print('Integer:',intNum,'Type:',type(intNum))
print("-"*30)

floatNum = 20.5
print('Float:',floatNum,'Type:',type(floatNum))
print("-"*30)

complexNum = 2+5j
print('Complex:',complexNum,'Type:',type(complexNum))
print("-"*30)

boolVal = True
print('Boolean:',boolVal,'Type:',type(boolVal))

print("\nOperations:")
print("int + float:", intNum+floatNum)
print("float + complex:", floatNum+complexNum)
print("int * bool:", intNum*boolVal)