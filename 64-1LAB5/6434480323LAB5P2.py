MY_USERNAME = "Ratchanon"

attempt = 0

username = input("Enter username : ")

while username != MY_USERNAME:
    attempt += 1
    # Too many attempts
    if attempt == 3:
        print("Not allowed. Incorrect name.")
        exit()
    username = input("Incorrect. Enter username : ")

print(f"Hello, {MY_USERNAME}")

