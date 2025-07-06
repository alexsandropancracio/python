num = int(input('Enter a number to calculate the factorial: '))
result = 1

for x in range(1, num + 1):
    result *= x
    if x < num:
        print(x, end=', ')
    else:
        print(x, end='')

print()

print(f'The factorial of {num} is: {result}')