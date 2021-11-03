# Add Item function
def add_item(items_list):
    itemToAdd = input("Enter item : ")
    
    if itemToAdd in items_list:
        print("Item is already in the list")
    else:
        items_list.append(itemToAdd)
        print("Item has been added")
    
    return items_list

# Change Item function
def change_item(items_list):
    itemToChange = input("Enter item : ")
    
    if itemToChange in items_list:
        newItem = input("Enter new item : ")
        
        if newItem in items_list:
            print("Item is already in the list")
        else:
            items_list[items_list.index(itemToChange)] = newItem
            print("Item has been changed")
    else:
        print("Item is not in the list")
    
    return items_list

# Insert Item function
def insert_item(items_list):
    itemToInsert = input("Enter item : ")
    
    if itemToInsert in items_list:
        print("Item is already in the list")
    else:
        location = int(input("Enter location that you want to insert:"))
        items_list.insert(location, itemToInsert)
        print("Item has been inserted")
    
    return items_list

# Remove Item function
def remove_item(items_list):
    itemToRemove = input("Enter item : ")
    
    if itemToRemove in items_list:
        items_list.remove(itemToRemove)
        print("Item has been removed")
    else:
        print("Item is not in the list")
    
    return items_list

# Show List function
def show_item(items_list):
    if items_list == []:
        print("The list is currently empty")
    else:
        print(items_list)

print("What would you like to do?")
print("1: add item")
print("2: change item")
print("3: insert item")
print("4: remove item")
print("5: show items")
print("6: exit")

items = []

while True:
    command = int(input("\nEnter a number: "))
    
    if command == 1:
        items = add_item(items)
    elif command == 2:
        items = change_item(items)
    elif command == 3:
        items = insert_item(items)
    elif command == 4:
        items = remove_item(items)
    elif command == 5:
        show_item(items)
    elif command == 6:
        break
    else:
        print("Invalid command")