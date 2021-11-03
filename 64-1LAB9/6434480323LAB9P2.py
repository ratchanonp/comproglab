def sum_digits(string):
    digits_list = [int(char) for char in string if char.isdigit()]
    return sum(digits_list)

print(sum_digits("zz1xa2d3"))
print(sum_digits("bb11c33"))
print(sum_digits("5432d"))
print(sum_digits("Hello"))