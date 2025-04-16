# Code Challenge 1-2-2

positive = 0
negative = 0
total = 0
number = 1
while number != 0:
    number = int(input("Enter an integer: "))
    if number > 0:
        positive += 1
        total += 1
    elif number < 0:
        negative += 1
        total += 1
print("Total Numbers: ",total," Positive Numbers: ", positive, "Negative Numbers: ", negative)

