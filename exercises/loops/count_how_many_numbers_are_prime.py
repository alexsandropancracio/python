start = int(input('Enter a number to start: '))
end = int(input('Enter a number to end: '))
total = []
result = 0


for x in range(start, end+1):
    if x <= 1:
        print(f'The number {x} is not prime, as it is less than or equal to 1.')
    else:
        prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            break
    if prime:
        result += 1
        total.append(x)
        
print(f'The prime numbers from {start} to {end} are:')
for z in total:
    if z != total[-1]:
        print(z, end=', ')
    else:
        print(z)
print(f'And the total numbers of prime numbers is: {result}')