import pprint

def pp(v):
    pprint.pprint(v)


#print(list(range(10)))

lista = [numero for numero in range(10)]#Isso é o mesmo que fazermos o loop abaixo, mas isso diretamente na lista.

sub_lista = [
    (x, y) 
    for x in range(2)
    for y in range(2)
]



#for numeros in range(10):
#    lista.append(numeros)

#print(lista)

produtos = [
    {'nome':'p1','preco':20},
    {'nome':'p2', 'preco': 10},
    {'nome': 'p2', 'preco':30}
]


novos_produtos = [#mapeamento - map()
    {**produto, 'preco': produto['preco'] * 1.05} #Aqui eu uso o kwargs por estar nomeando os parâmetros de um dicionário, se fosse uma lista eu usava args.
    if produto['preco'] > 20 else {**produto} #ternário
    for produto in produtos
    if produto['preco'] > 10 #filtro
]

print(sub_lista)

print()
print(*produtos, sep='\n')

print()
print(novos_produtos)

print()
print(*novos_produtos)

print()
pp(novos_produtos)