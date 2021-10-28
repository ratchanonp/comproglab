yesterday_case = int(input("Enter yesterday of case : "))
today_case = int(input("Enter today of case : "))

total_case = yesterday_case + today_case
highest_case = max(yesterday_case, today_case)

while today_case >= yesterday_case:
    yesterday_case = today_case
    if today_case > yesterday_case:
        print(f"Danger Case is increase")
        
    today_case = int(input("Enter today of case : "))
    total_case += today_case
    print(f"Total case : {total_case}",end=" ")
    
    if today_case > highest_case:
        highest_case = today_case
        print(f"RED CODE!! New high : {highest_case}",end=" ")
        
    
    print()

print(f"Good Situation")