lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Luiz'}
]

for item in lista:
    if isinstance(item, set):#Se o item é do tipo set
        print('SET')
        item.add(5)#Adiciona o número 5
        print(item)#Mostra pra mim o que só é set no item.

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item)

    else:
        print('OUTRO')
        print(item)
