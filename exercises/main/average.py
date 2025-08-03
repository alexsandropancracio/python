numbers = [2,4,6,8,10]

def average(num):
    sum = 0
    for x in num:
        sum += x
    total = sum / len(num)
    return total

print(average(numbers))