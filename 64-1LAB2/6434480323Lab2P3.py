a, b, c = input("Length of 3 sides: ").split(",")
a, b, c = float(a), float(b), float(c)

# Can create triangle with 3 sides
isTriangle = a + b > c and a + c > b and b + c > a

print(f"Triangle : {isTriangle}")