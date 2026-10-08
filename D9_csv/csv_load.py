import csv
from pathlib import Path

p = Path(__file__).parent / "data"
student = p / "students.csv"
correctrows_count = 0
jump = 0
score_list = []
with open(student,'r',encoding = 'utf-8') as f:
    for row in csv.DictReader(f):
        if len(row) == 3:
            try:
                score = float(row['score'])
                score_list.append(score)
                correctrows_count += 1
            except ValueError:
                jump += 1
                continue
        else:
            jump += 1
    avg_score = sum(x for x in score_list) / len(score_list)

print(f"有效行数:{correctrows_count}")
print(f"跳过行数:{jump}")
print(f"平均分数:{avg_score}")

