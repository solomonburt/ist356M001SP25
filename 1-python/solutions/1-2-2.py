# Challenge 1-2-2

count = 0
positive =0 
negative =0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    count += 1
    if number > 0:
        positive += 1
    else:
        negative += 1
print(f"Total numbers entered: {count}")
print(f"Negative numbers: {negative}")
print(f"Positive numbers: {positive}")