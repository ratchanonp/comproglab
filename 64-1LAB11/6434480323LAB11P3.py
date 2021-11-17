score_file = "./score.txt"

competitors = {}

with open(score_file, 'r') as f:
    for line in f:
        values = line.strip().split()
        competitor = values[0]
        sum_score = sum(map(int, values[1:]))
        competitors[competitor] = sum_score

    highest = []
    for competitor, score in competitors.items():
        highest.append((competitor, score))

    highest.sort(key=lambda x: x[1], reverse=True)

    print("The winners are :")
    for i in range(3):
        print(f"{i} : {highest[i][0]} {highest[i][1]}")