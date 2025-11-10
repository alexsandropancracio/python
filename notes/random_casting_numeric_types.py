import random
i = 10
f = 5.0
c = 1j

x = i

num = [
    random.randrange(0,50),#Aqui entendemos que devemos colocar um valor inicial e outro final do tipo inteiro.
    random.randrange(0,50),
    random.randrange(0,50),
    random.randrange(0,50)
]

print('Valor da variável: ' + str(x) + ' Tipo: ' + str(type(x))) #Aqui observamos a operação de casting, onde convertemos um tipo numérico inteiro para string e um tipo para string também.

#O casting pode converter uma variável para qualquer outro tipo de dados, como o float ou complex e entre outros. Por exemplo:

x = int(f)

print(x)

print('Valor: ' + str(num[0]) + ' Tipo: ' + str(type(num)))
print('Valor: ' + str(num[1]) + ' Tipo: ' + str(type(num)))
print('Valor: ' + str(num[2]) + ' Tipo: ' + str(type(num)))
print('Valor: ' + str(num[3]) + ' Tipo: ' + str(type(num)))