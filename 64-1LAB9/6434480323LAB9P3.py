containWith = int(input("Enter a number between [0,9]: "))

if containWith >= 0 and containWith <= 9:
    # Find Number between 1 - 100 contain with containWith
    hasContainWith = [x for x in range(1, 100) if str(containWith) in str(x)]
    print(hasContainWith)
else:
    print("The number is not between [0,9]")