start = int(input('Enter a number to start: '))
end = int(input('Enter a number to end: '))
result = 0

for x in range(start, end +1):
    for y in range(1, x + 1):
        if y * y == x:
            print(f'{x} is a perfect square: ({y} * {y})')
            result += x
            break

print(f'And the sum of perfect squares are: {result}')