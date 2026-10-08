import csv
from pathlib import Path

p = Path(__file__).parent / "data"
student = p / "students.csv"
correctrows_count = 0
jump = 0
score_list = []
avg_score = 0

with open(student,'r',encoding = 'utf-8') as f:
    for row in csv.DictReader(f):
        try:
            name = row['name']
            subject = row['subject']
            score = float(row['score'])
            if not name or not subject:
                raise ValueError("字段缺失")
            score_list.append(score)
            correctrows_count += 1
        except (ValueError,TypeError):
            jump += 1
            continue
    if score_list:
        avg_score = sum(score_list) / len(score_list)

print(f"有效行数:{correctrows_count}")
print(f"跳过行数:{jump}")
print(f"平均分数:{avg_score}")

