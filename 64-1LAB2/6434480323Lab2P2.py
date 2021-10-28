a, b, c = input("Enter coefficients a, b, c : ").split(",")
a, b, c = float(a), float(b), float(c)

# Can solve with quadratic formula
canSolve = a != 0 and (b**2 - 4*a*c) >= 0

print(f"Can use quadratic formula : {canSolve}") 