
first = int(input('Enter a number to start: '))
last = int(input('Enter a number to end: '))

total = 0
    
if first < last:
    for x in range(first, last + 1):
        total += x
        if x % 2 == 0:
            print(x)
else:
    for y in range(first, last - 1, -1):
        total += y
        if y % 2 == 0:
            print(y)


print('The total value summed between them is: ', total)



