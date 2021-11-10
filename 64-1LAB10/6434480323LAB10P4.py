coffeeData = {
    "Cappuccino": {
        "S": 60,
        "L": 70
    },
    "Espresso": {
        "S": 45,
        "L": 50
    },
    "Latte": {
        "S": 65,
        "L": 75
    },
}

drink, size, quantity = input("Enter drink, size and number : ").split()
quantity = int(quantity)

if drink in coffeeData:
    if size in coffeeData[drink]:
        print(f"Total : {quantity * coffeeData[drink][size]}")
    else:
        print("Incorrect size.")
else:
    print("Drink not available.")
