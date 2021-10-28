from random import randint

num = int(input("Number : "))
rand = randint(1, 9)

while num != rand:
    print(f"Guess {rand}")
    if rand > num:
        print("Too High")
        rand = randint(1 ,rand)
    elif rand < num:
        print("Too Low")
        rand = randint(rand, 9)

print("You Win")
