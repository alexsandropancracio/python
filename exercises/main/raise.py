def validar_entrada(n, d):
    if not isinstance(n, (int, float)):
        raise TypeError('O numerador não é um número.')
    if not isinstance(d, (int, float)):
        raise TypeError('O denominador não é um número.')
    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')

def dividir(n, d):
    validar_entrada(n, d)
    return n / d

try:
    print(dividir(8, '1'))
except Exception as e:
    print('Erro:', type(e).__name__, '-', e)

try:
    print(dividir(8, 0))
except Exception as e:
    print('Erro:', type(e).__name__, '-', e)

try:
    print(dividir(8, 2))
except Exception as e:
    print('Erro:', type(e).__name__, '-', e)
