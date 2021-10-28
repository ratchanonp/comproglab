from random import randint
rand = randint(1, 9)

guess = int(input("Your Guess : "))
while guess != rand:
    guess = int(input("Your Guess : "))

print("Correct.")