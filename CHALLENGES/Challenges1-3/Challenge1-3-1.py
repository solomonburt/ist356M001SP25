# Challenge 1-3-1
def average(numbers):
    sumOfInt = 0
    for i in numbers:
        sumOfInt += i
    avrg = sumOfInt/len(numbers)
    return avrg

a = average([10, 20, 15])
print(a)