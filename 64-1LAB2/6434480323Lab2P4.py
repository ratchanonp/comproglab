a, b, c = input("Length of 3 sides: ").split(",")
a, b, c = float(a), float(b), float(c)

# Check is Right Triangle
isRightTriangle = (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2

print(f"Right triangle: {isRightTriangle}")