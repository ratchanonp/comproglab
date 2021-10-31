from numpy import dot
file = "vectors.txt"

with open(file) as file:
    vectors = [list(map(float,line.strip().split())) for line in file]
    
    for i, vector in enumerate(vectors,1):
        print(f"v{i} =")
        print(f"{vector}")
    
    # Check Vector in same size
    if len(vectors[0]) != len(vectors[1]):
        print("Incompatible size")
    else:
        # Dot Product vector
        result = dot(vectors[0], vectors[1])
        print(f"v1*v2 = {result}")