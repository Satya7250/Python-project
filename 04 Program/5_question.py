#Write a program to find the largest element among three Numbers.

a = 10
b = 25
c = 15

# Finding the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)
