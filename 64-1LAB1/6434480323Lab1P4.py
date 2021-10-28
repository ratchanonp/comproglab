name = input("Name: ")
age = int(input("Age: "))

birthyear = 2564 - age

print(f"{name}{birthyear%100}@chula.ac.th")