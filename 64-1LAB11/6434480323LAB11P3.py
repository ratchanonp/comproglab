score_file = "./score.txt"

competitors = {}

with open(score_file, 'r') as f:
    for line in f:
        values = line.strip().split()
        competitor = values[0]
        sum_score = sum(map(int, values[1:]))
        competitors[competitor] = sum_score

    highest3 = []
    for competitor, score in competitors.items():
        highest3.append((competitor, score))

    highest3.sort(key=lambda x: x[1], reverse=True)

    print("The winners are :")
    for i in range(3):
        print(f"{i} : {highest3[i][0]} {highest3[i][1]}")