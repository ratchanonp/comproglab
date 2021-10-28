def f(x):
    # factorial
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return 1 / fact

def summation(a, b):
    a, b = min(a, b), max(a, b)
    
    sum = 0
    for i in range(a, b+1):
        sum += f(i)
    
    return sum

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print(summation(m, n))