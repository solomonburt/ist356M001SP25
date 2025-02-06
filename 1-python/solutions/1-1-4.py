# Code Challenge 1-1-4
grade = int(input("Enter your grade: "))

if grade < 120 and grade > 0:
    if grade > 95:
        letter = "A"
    elif grade <=95 and grade >=75:
        letter = "B"
    elif grade <75 and grade >=50:
        letter = "C"
    else:
        letter = "F"
else:
    letter = "Invalid grade"

print(f"Your grade is {grade}, which gives you {letter}")

