

# Function to check if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,50):
        if i == n:  
            continue
        if n % i == 0:
            return False
    return True

print("Prime numbers between 20 and 50 are:")
for num in range(20, 51):
    if isPrime(num):
        print(num, end=" ")
