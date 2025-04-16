# Code Challenge 1-1-4

grade = int(input("Enter the college class grade (0-120): "))
letterGrade = ""
if grade <= 120 and grade >= 0:
    if grade >= 95:
        letterGrade = "A"
    elif grade >= 75:
        letterGrade = "B"
    elif grade >= 50:
        letterGrade = "C"
    else:
        letterGrade = "F"
else:
    print("Invalid grade value!")
print(letterGrade)