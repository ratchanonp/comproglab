subjectData = {
    "2301117": ("Calculus I",4),
    "2301118": ("Calculus II",4),
    "2301286": ("Probability and Statistics",3),
    "2301399": ("Project Proposal",1),
    "2301499": ("Senior Project",2),
    "2302113": ("General Chemistry Lab I",1),
    "2302161": ("General Chemistry",3)
}


courseID = input("Course ID: ")

while courseID != "0":
    subject = subjectData.get(courseID)
    if subject is None:
        print("Unknow\n")
    else:
        print(f"{subject[0]} {subject[1]}\n")

    courseID = input("Course ID: ")
