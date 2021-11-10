file = "./Lab10_2_conversation.txt"

wordCount = {}

with open(file, 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            word = word.strip(':?,.')
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

    for word, count in wordCount.items():
        print(word, count)
