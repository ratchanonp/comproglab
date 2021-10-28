from math import sqrt
num = int(input("Enter number : "))

for i in range(2, round(num + 1)):
    if num % i == 0:
        isPrime = True
        for j in range(2, round(sqrt(i) + 1)):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)