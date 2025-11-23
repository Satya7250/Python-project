def sum(num):
    if num == 1:
        return 1
    return sum(num - 1) *num
result = sum(5)
print(result)
