first = int(input('Enter a number to start: '))
last = int(input('Enter a number to last: '))

total = 0

for x in range(first, last + 1):
    if x % 2 != 0:
        total += x
        if x < last - 1:
            print(x, end=' + ')
        else:
            print(x, end='')

print()
print('The sum of the number between', first, 'and', last, 'is:', total)


