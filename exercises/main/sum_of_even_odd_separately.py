num = int(input('Enter a number to start: '))
result = 0
total = 0

print('Even Numbers:')
for x in range(1, num + 1):
    if x % 2 == 0:
        result += x
        print(x)

print()
print('Odd Numbers:')    
for y in range(1, num + 1):
    total += y
    if y % 2 != 0:
        print(y)

print()
print('Total of the sum of even numbers:', result)
print('Total of the sum of odd numbers:', total)