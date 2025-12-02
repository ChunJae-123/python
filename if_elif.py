# if_elif.py

score = int(input("insert your score!! : "))

if 100 >= score >= 90:
    grade = "A"
if 90 > score >= 80:
    grade = "B"
if 80 > score >= 70:
    grade = "C"
if 70 > score >= 60:
    grade = "D"
if 60 > score:
    grade = "E"

print("your grade is : " + grade)