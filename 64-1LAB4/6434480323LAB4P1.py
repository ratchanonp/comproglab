from math import pi

shape = input("Choose circle, squre or rectangle : ")


# Circle 
if shape == "circle":
    radius = float(input("Length of the radius of the circle : "))
    
    area = pi * radius ** 2
    print(f"Area is {area}")
# Squre
elif shape == "square":
    side = float(input("Length of the side of the square : "))
    
    area = side ** 2
    print(f"Area is {area}")
# Rectangle
elif shape == "rectangle":
    width, height = input("Length of two sides of the rectangle : ").split(",")
    width, height = float(width), float(height)
    
    area = width * height
    print(f"Area is {area}")
# Invalid shape
else:
    print("Invalid choice.")