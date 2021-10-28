prev_temp = float(input(f"Day 1 : "))

for day in range (2, 8):
    temp = float(input(f"Day {day} : "))
    if temp < prev_temp:
        print(f"Temperature dropped on day {day}")
    prev_temp = temp