end = int(input('Enter a number to start: '))
result = 0

for x in range(1, end + 1):
    if x % 3 == 0 and x % 2 != 0:
        result += 1
        print(x)

print('Total numbers divisible to 3 is:', result)