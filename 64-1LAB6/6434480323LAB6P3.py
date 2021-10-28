from math import sqrt

num = int(input("Enter an integer : "))
isPrime = True

for i in range(2, int(sqrt(num))):
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")