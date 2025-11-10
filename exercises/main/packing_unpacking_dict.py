a,b = 1,2
a,b = b,a

pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza'
}

a, b = pessoa
print(a,b)

b, c = pessoa.items()
print(b,c)

(c1,c2), (d1,d2) = pessoa.items()
print(c1,c2)#Aqui temos o empacotamento da primeira chave e valor.
print(d1,d2)
print()

for chave, valor in pessoa.items():
    print(chave, valor)

dados_pessoa = {
    'idade': 28,
    'altura': 1.73
}

pessoa_completa = {**pessoa, **dados_pessoa}#Isso aqui é o desempacotamento de um dicionário
#print(pessoa, dados_pessoa)

def mostra_argumentos_nomeados(*args, **kwargs):
    print()
    print('Argumentos não nomeado vai pra args: ')
    print(args)
    print()

    print('Argumentos nomeados vai para kwargs:')
    for chave, valor in kwargs.items():
        print(chave,valor)

mostra_argumentos_nomeados(1, 2, nome='Maria', idade=20)
