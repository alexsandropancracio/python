first = int(input('Enter a number to start: '))
last = int(input('Enter a number to end: '))
mult = int(input('Enter a number to know the multiple: '))

if first < last:
    print('The multiple of', mult, 'between', first, 'and', last, 'are:')
    for x in range(first, last + 1):
        if x % mult == 0:
            print(x)
else:
    print('The multiple of', mult, 'between', first, 'and', last, 'are:')
    for y in range(first, last - 1, -1):
        if y % mult == 0:
            print(y)