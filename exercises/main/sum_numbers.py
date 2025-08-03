while True:

    first = int(input('Enter a number to start: '))
    last = int(input('Enter a number to end: '))

    if first >= last:
        print('Sorry, but the sum of the numbers must be in ascending order. Example: 1 to 10. Please, try again.')
    else:
        break

total = 0

for x in range(first, last):
    total += x

print('The sum of the number between', first, 'and', last, 'is:', total)

