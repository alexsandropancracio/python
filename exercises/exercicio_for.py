code = "Python"

for x in code:
    print(x, end='')

for y in range(5):#loop em forma crescente.
    print(y)
    
for w in range(10, -1, -2):#loop em forma decrescente parametrizada.
    print(w)

for z in range(0, 10, +2):#loop em forma crescente parametrizada
    print(z)

#No range temos 3 parâmetros, conhecidos como start, stop e step. Se o start for menor que o stop com o step negativo, o código não funciona.

soma = 0

for i in range(5):
    num = float(input(f'Digite o {i+1}º número: '))
    total = soma + num
    
print('A soma dos valores são: ' + str(total))