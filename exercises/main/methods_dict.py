# Métodos úteis do dicionário em Python
# len - quantas chaves tem o dicionário
# keys - iterável com as chaves
# values - iterável com valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave específica (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro

import copy

pessoa = {
    'nome': 'Alexsandro',
    'idade': 28,
    #'cidade': 'Carapicuíba'
}

#print(pessoa.__len__()) aqui usamos no modo dander.
print(len(pessoa))
print(pessoa.keys())#Aqui temos uma dict_items e precisamos fazer a coerção.
print()


pessoa.setdefault('cidade', 'Osasco')#Aqui é meio que caso não haja esse campo, temos um valor padrão.
coercao = list(pessoa)

print(coercao)

print('\nChaves:')
for chaves in pessoa.keys():
    print(chaves)

print('\nValores:')
for valores in pessoa.values():
    print(valores)

print('\nChaves e Valores:')
for chave, valor in pessoa.items():#Aqui temos a mesma ideia com o enumerate() usamos duas variáveis.
    print(chave, valor)

#Shallow Copy & Deep Copy

a1 = {
    'b1': 1,
    'b2': 2,
    'l1': [0,1,2]
}

a2 = a1

a3 = copy.deepcopy(a1)

print()
print(a3)

a2['b1'] = 100
a2['l1'][1] = 999

print()
print(a1)#aqui percebemos que mesmo armazenando o "a1" no "a2", modificando "a2" consequentemente modificamos também "a1", pois estão todos na mesma memória.
print(a2)#percebemos também que sublistas elas são linkadas e não copiadas, caso venhamos modificar elas na shallow copy, as sublistas também são alteradas.

#Pra isso usamos a biblioteca copy importando o deepcopy, pois assim fazemos uma cópia profunda sem alterar a variável principal de onde fizemos a cópia.

print()
sobrenome = pessoa.popitem()
print(sobrenome)

print()
pessoa.update({
    #aqui posso criar uma nova chava ou atualizar uma chave existente
    #'nome': 'novo valor'
})

a2.update(b1='Eli', b2=46)#ao invés de usarmos chaves, podemos usar parâmetros nomeados.
print(a2)