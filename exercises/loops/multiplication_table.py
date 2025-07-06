while True:
    num = int(input('Enter a number from 1 to 10 to check the multiplication table: '))

    if num > 10:
        print('the numbers for the multiplication table are from 1 to 10. Please try again.')
    else:
        break

print(f'The multiplication table of {num} is:')
for z in range(1, 11):
    total = num * z
    print(num, 'x', z, '=', total)

