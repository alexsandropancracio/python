start = int(input('Enter a number to start: '))
end = int(input('Enter a number to end: '))
total = 0
result = 0

if start < end:
    for x in range(start, end + 1):
        if x % 3 == 0 and x % 5 == 0:
            total += 1
            result += x
            print(x)
else:
    for y in range(start, end - 1, -1):
        if y % 3 == 0 and y % 5 == 0:
            total += 1
            result += y
            print(y)

print('Total numbers: ', total)
print('Result: ', result)