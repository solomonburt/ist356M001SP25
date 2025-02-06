def average (list_of_numbers):
    total = 0
    count = 0

    for number in list_of_numbers:
        total += number
        count += 1
    return total/count


nums = [10, 20, 10, 5]
avg = average(nums)
print(f"Average of {nums} is {avg}")