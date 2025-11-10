import os
os.system('cls')

try:
    num = input('Digite um número para saber se é par ou ímpar: ')
    num_int = int(num)

    if num_int % 2 == 0:
        print(f'{num_int} é par.')
    else:
        print(f'{num_int} é ímpar.')
except:
    print('Digite somente números inteiro. Tente novamente!')
