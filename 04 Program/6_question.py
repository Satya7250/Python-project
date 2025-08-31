#Write a program to print the sum of all the even numbers in the range 1 - 50 and print the even sum.

evenSum = 0

for num in range(1, 51):
    if num % 2 == 0:
        evenSum += num

print("Sum of even numbers:", evenSum)
