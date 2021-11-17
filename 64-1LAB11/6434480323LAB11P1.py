stocks = {}

for i in range(10):
    id, size, quantity = input("Enter product ID, size, number of items : ").split()
    id, quantity = int(id), int(quantity)
    
    if id not in stocks:
        stocks[id] = {}
    if size not in stocks[id]:
        stocks[id][size] = quantity
    if size in stocks[id]:
        stocks[id][size] += quantity


print("\nStocks:")

sorted_stocks = sorted(stocks.items(), key=lambda x: x[0])
for id, data in sorted_stocks:
    sorted_data = sorted(data.items(), key=lambda x: x[0])
    for size, quantity in sorted_data:
        print(f"{id} {size} {quantity}")