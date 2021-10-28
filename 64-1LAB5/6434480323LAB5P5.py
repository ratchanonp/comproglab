balance = 50000

while balance > 0:
    withdraw = float(input("withdraw : "))
    if withdraw > balance:
        print("Insufficient fund.")
    else:
        balance -= withdraw

print(f"Balance is {balance:.0f}.")