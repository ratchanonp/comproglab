studentScore = {}
file = "./studentScore.txt"

with open(file, "r") as f:
    for line in f:
        (key, val) = line.split()
        studentScore[key] = val

    # Sort the dictionary by value
    sortedStudentScore = sorted(studentScore.items(),
                                key=lambda item: item[1],
                                reverse=True)

    # Print the sorted dictionary
    for student, score in sortedStudentScore:
        print(student)
