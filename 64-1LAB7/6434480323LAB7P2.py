file = "./move_23.txt"

with open(file, 'r') as commands:
    pos_x, pos_y = map(int, input("Initial position : ").split(","))
    
    wall_x1, wall_y1 = -10, -10
    wall_x2, wall_y2 = 10, 10
    
    for command in commands:
        command = command.strip()
        if command == "U" and pos_y + 1 < wall_y2:
            pos_y += 1
        elif command == "D" and pos_y - 1 > wall_y1:
            pos_y -= 1
        elif command == "L" and pos_x - 1 > wall_x1:
            pos_x -= 1
        elif command == "R" and pos_x + 1 < wall_x2:
            pos_x += 1
        elif command not in ["U", "D", "L", "R"]:
            print("Invalid command")
            exit()
    
    print(f"Robot stops at {pos_x},{pos_y}")

