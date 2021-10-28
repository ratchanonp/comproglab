stdID = input("Enter student ID : ")

# 10 Digit
is10Digit = len(stdID) == 10

stdID = int(stdID)

# 2 First digit between 50 - 64
year = (stdID // 100000000)
isYear_btw50_64 = year >= 50 or year <= 64

# Third digit is 3, 4 or 7
degree = (stdID // 10000000) % 10
isDegree3_4_7 = degree == 3 or degree == 4 or degree % 10 == 7

# 2 Last digit is between 21 - 28
faculty = stdID % 100
isFaculty_btw21_28 = faculty >= 21 or faculty <= 28

# Check if all conditions are true
if is10Digit and isYear_btw50_64 and isDegree3_4_7 and isFaculty_btw21_28:
    # Do the task
    semester = int(input("Enter semester : "))
    
    if semester in [1, 2, 3]:
        # Year = 50 - 55
        if year >= 50 and year <= 55:
            # Group 1 [21 23 25 28]
            if faculty in [21, 23, 25, 28]:
                # Bachlor Degree
                if degree == 3 or degree == 4:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 18000
                    # Semester 3
                    elif semester == 3:
                        fee = 4500
                # Master Degree
                elif degree == 7:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 26000
                    # Semester 3
                    elif semester == 3:
                        fee = 7000
            # Group 2 [22 24 26 27]
            if faculty in [22, 24, 26, 27]:
                # Bachlor Degree
                if degree == 3 or degree == 4:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 14500
                    # Semester 3
                    elif semester == 3:
                        fee = 4500
                # Master Degree
                elif degree == 7:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 19000
                    # Semester 3
                    elif semester == 3:
                        fee = 7000
        # Year >= 56
        elif year >= 56:
            # Group 1 [21 23 25 28]
            if faculty in [21, 23, 25, 28]:
                # Bachlor Degree
                if degree == 3 or degree == 4:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 21000
                    # Semester 3
                    elif semester == 3:
                        fee = 5250
                # Master Degree
                elif degree == 7:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 31000
                    # Semester 3
                    elif semester == 3:
                        fee = 7750
            # Group 2 [22 24 26 27]
            if faculty in [22, 24, 26, 27]:
                # Bachlor Degree
                if degree == 3 or degree == 4:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 17000
                    # Semester 3
                    elif semester == 3:
                        fee = 5250
                # Master Degree
                elif degree == 7:
                    # Semester 1/2
                    if semester == 1 or semester == 2:
                        fee = 23000
                    # Semester 3
                    elif semester == 3:
                        fee = 7750
        print(f"Registration fee : {fee:,}")
    else:
        print("Invalid semester")
else:
    print("Invalid ID")