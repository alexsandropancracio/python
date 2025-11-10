#CRUD - Dicionário

pessoa = {}

pessoa['nome'] = 'Alexsanndro'
pessoa['sobrenome'] = 'Ramos'
pessoa['idade'] = 28
pessoa['endereço'] = 'Rua Formosa'
pessoa['cidade'] = 'Osasco'

pessoa['cidade'] = 'Carapicuíba'

del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print('Essa chave não existe.')
else:
    print(pessoa['sobrenome'])

print(pessoa)