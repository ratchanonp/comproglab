x, y = input("x,y : ").split(",")
x, y = float(x), float(y)

# Sqaure a
ax1 , ay1 = 0, 0
ax2 , ay2 = 40,40

# Sqare b
bx1 , by1 = -40, -20
bx2 , by2 = 10, 20

# C is intersect of a and b
isInA = x > ax1 and x < ax2 and y > ay1 and y < ay2
isInB = x > bx1 and x < bx2 and y > by1 and y < by2

if isInA and isInB:
    print(f"( {x} , {y} ) is in C")
elif isInA:
    print(f"( {x} , {y} ) is in A")
elif isInB:
    print(f"( {x} , {y} ) is in B")
else:
    print(f"( {x} , {y} ) is in D")


