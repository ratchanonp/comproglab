alphabet = input("Enter Uppercase Alphabet : ")

if alphabet.isupper():
    count_to = int(input("Enter Number : "))

    new_alphabet = ((ord(alphabet) + (count_to % 26)))
    
    if new_alphabet > 90:
        new_alphabet = new_alphabet - 26
    
    print(chr(new_alphabet))
else:
    print("Please Enter Uppercase Alphabet")