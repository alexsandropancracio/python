total = 0

for x in range(0, 51, 2):
    if x < 50:
        total = total + 1
        print(x, end=', ')
    else:
        print(x, end='.')
    
print()

print('In total I have', total, 'even numbers.')