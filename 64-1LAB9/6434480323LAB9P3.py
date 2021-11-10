containWith = int(input("Enter a number between [0,9]: "))

if containWith >= 0 and containWith <= 9:
    # 2 - 99
    hasContainWith = [x for x in range(2, 100) if str(containWith) in str(x)]
    print(hasContainWith)
else:
    print("The number is not between [0,9]")