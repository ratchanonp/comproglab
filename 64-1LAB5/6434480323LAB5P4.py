n_student = int(input("Number of students : "))

sum_pass = 0
sum_fail = 0

count_pass = 0
count_fail = 0

hightest_score = 0

PASS_SCORE = 5

for i in range(n_student):
    score = float(input(f"Student {i+1} : "))
    
    if score >= PASS_SCORE:
        sum_pass += score
        count_pass += 1
    else:
        sum_fail += score
        count_fail += 1
    # Highest Score
    if score > hightest_score:
        hightest_score = score

avg = (sum_pass + sum_fail) / n_student
avg_pass = (sum_pass / count_pass) if count_pass != 0 else 0
avg_fail = (sum_fail / count_fail) if count_fail != 0 else 0

print(f"Average score : {avg}")
print(f"Average passing score : {avg_pass}")
print(f"Average failing score : {avg_fail}")
print(f"Highest score : {hightest_score}")
