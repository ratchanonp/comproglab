file = "./move_12.txt"

with open(file, 'r') as commands:
    pos_x, pos_y = map(int, input("Initial position : ").split(","))
    
    for command in commands:
        command = command.strip()
        if command == "U":
            pos_y += 1
        elif command == "D":
            pos_y -= 1
        elif command == "L":
            pos_x -= 1
        elif command == "R":
            pos_x += 1
        else:
            print("Invalid command")
            exit()
    
    print(f"Robot stops at {pos_x},{pos_y}")

