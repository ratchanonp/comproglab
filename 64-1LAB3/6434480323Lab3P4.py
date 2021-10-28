stdID = input("Enter student ID : ")

# 10 Digit
is10Digit = len(stdID) == 10

stdID = int(stdID)

# 2 First digit between 50 - 64
first2Digit = (stdID // 100000000)
isFirst2_btw50_63 = first2Digit >= 50 or first2Digit <= 64

# Third digit is 3, 4 or 7
thirdDigit = (stdID // 10000000) % 10
isThird3_4_7 = thirdDigit == 3 or thirdDigit == 4 or thirdDigit % 10 == 7

# 2 Last digit is between 21 - 28
last2digit = stdID % 100
isLast2_btw21_28 = last2digit >= 21 or last2digit <= 28

# Check if all conditions are true
if is10Digit and isFirst2_btw50_63 and isThird3_4_7 and isLast2_btw21_28:
    print("Valid ID")
else:
    print("Invalid ID")