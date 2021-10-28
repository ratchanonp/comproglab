word = input("Next Word : ")

sentence = ""

while word != ".":
    sentence += word + " "
    word = input("Next Word : ")

print(f"Sentence : {sentence}")