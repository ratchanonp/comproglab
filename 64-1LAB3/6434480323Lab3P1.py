from math import sqrt

a, b, c = input("Enter coefficients a, b, c : ").split(",")
a, b ,c = float(a), float(b), float(c)

root = (b ** 2) - (4 * a * c)

if root < 0 and a == 0:
    print("No real solution")
else:
    x1 = (-b + sqrt(root)) / (2 * a)
    x2 = (-b - sqrt(root)) / (2 * a)
    
    print(f"x = {x1}, {x2}")