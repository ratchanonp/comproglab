sol_file = "sol.txt"
exam_file = "exam.txt"

with open(sol_file, "r") as sols, open(exam_file, "r") as exams:
    sols = sols.readline().strip().split()
    exams = [exam.strip().split() for exam in exams]
    
    student_score = [0 for _ in range(len(exams))]
    question_score = [0 for _ in range(len(sols))]
    
    for i in range(len(exams)):
        for j in range(len(sols)):
            if exams[i][j] == sols[j]:
                student_score[i] += 1
                question_score[j] += 1
    
    print(f"Student score: \n{student_score}\n")
    
    for i, score in enumerate(question_score, 1):
        print(f"Question {i}: {score/len(exams)}")
    
    print()
    
    q_hardest = [i for i, score in enumerate(question_score, 1) if score == min(question_score)]
    q_easiest = [i for i, score in enumerate(question_score, 1) if score == max(question_score)]
    
    print(f"{' '.join(list(map(str, q_hardest)))} is the hardest question.")
    print(f"{' '.join(list(map(str, q_easiest)))} is the easiest question.")