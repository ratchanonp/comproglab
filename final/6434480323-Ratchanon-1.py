"""
Name : Ratchanon Panmas
ID : 6434480323
Section : 2
"""

transcript_file = "./transcript.txt"

sum_grade = 0
sum_credit = 0

with open(transcript_file, "r") as transcript:
    for line in transcript:
        line = line.strip()
        courseId, credit, grade = line.split()
        sum_grade += float(credit) * float(grade)
        sum_credit += float(credit)
    
    gpax = sum_grade / sum_credit
    print(f"GPAX : {gpax}")