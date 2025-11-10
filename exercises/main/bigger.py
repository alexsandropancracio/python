numbers = [1,2,3,4,5,6,7,8,9]

def maior_lista(num):
    total = num[0]
    for x in num:
        if x > total:
            total = x
    return total

print(maior_lista(numbers))