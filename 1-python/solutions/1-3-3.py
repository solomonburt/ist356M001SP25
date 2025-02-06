import json

text = input("Enter names and grades: ")
students = []
for student in text.split(","):
    name, grade = student.strip().split()
    grade = float(grade)
    students.append({"name": name, "grade": grade})

with open("students.json", "w") as file:
    json.dump(students, file)