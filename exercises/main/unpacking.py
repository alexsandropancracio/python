string = 'ABC'
lista = ['a','b','c',1,2,3,'e','f']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Alex', 'Eli', 'Vera'],
    ['Junior', 'Antonio', 'Juan']
]

print(*salas, sep='\n')

p,s,*_,ap,u = lista
print(p,u)

print(*lista)

for itens in lista:
    print(itens, end=' ',)

