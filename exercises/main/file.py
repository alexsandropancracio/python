if 1 and 1:
    print(True and 0 and True)

valor = input('Digite um número: ')

try:
    valor_int = int(valor)
    print(f'O dobro de {valor} é: {valor_int * 2}')
except:
    print('Isso não é um número. Tente novamente!')