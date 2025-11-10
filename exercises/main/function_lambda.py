# Função lambda em python.
# A função lambda é uma função como qualquer outra em python.
# Porém, são funções anônimas que contenham uma linha.
# Ou seja, tudo deve ser contido em uma única expressão.
lista = [
    {'nome': 'Alexsandro', 'sobrenome': 'Ramos'},
    {'nome': 'Elisangela', 'sobrenome': 'Ramos'},
    {'nome': 'Verialva', 'sobrenome': 'Queiroz'},
    {'nome': 'Marcos', 'sobrenome': 'Tamaguchi'},
    {'nome': 'Antonio', 'sobrenome': 'Pereira'},
]

def exibir(dicionario):
    for itens in dicionario:
        print(itens)

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y


#def ordena(item):
#    return item['nome']
#Como definimos o key para a função no sort(), definimos então por qual chave do dicionário devemos ordenar, se é pela chave "nome" ou "sobrenome".

lista.sort(key=lambda item: item['nome'])#lambda seria def e lambida vai direto pros parâmetros, ela também é uma função sem nome.
#lista.sort(key=ordena) #O método sort() serve pra ordenarmos a lista
#Há outra forma que ordena a lista também que é o "sorted(lista)"

#Pra termos uma shallow copy dessa ordenação nós usamos o sorted:

ordenacao = sorted(lista, key=lambda item: item['sobrenome'])

exibir(ordenacao)
print()
exibir(lista)

print(
    executa(
        lambda x, y: x + y, 2, 3
    ),
    executa(soma, 2, 3)
)

duplica = executa(
    lambda m: lambda n: n * m, 2
)
print(duplica(2))

