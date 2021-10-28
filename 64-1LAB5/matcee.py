

attempt = 0

username = input("Enter username : ")

while username != "Matcee":
    attempt += 1
    # Too many attempts
    if attempt == 3:
        break
    username = input("Incorrect. Enter username : ")

print(f"Hello, {MY_USERNAME}")