produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

print(produto.items())
print()

for chave,valor in produto.items():
    print(chave, valor)
print()

dc_comprehension = {
    chave: valor
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dc_comprehension)