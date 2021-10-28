MY_USERNAME = "Ratchanon"

username = input("Enter username : ")

while username != MY_USERNAME:
    username = input("Incorrect. Enter username : ")

print(f"Hello, {MY_USERNAME}")