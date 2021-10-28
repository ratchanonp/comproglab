from math import sqrt

a, b, c = input("Enter coefficients a, b, c : ").split(",")
a, b, c = float(a), float(b), float(c)

# find roots from Quadratic Formala
x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)

print(f"x = {x1} , {x2}")