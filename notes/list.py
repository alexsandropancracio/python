carros = ['HRV', 'Golf', 'Argo', 'Focus']
pecas = ['Pneu', 'Motor', 'Suspenção', 'Bancos']

print(carros[-1]) #Aqui observamos que com o número negativo, ela vai na forma decrescente na list.
print(carros[0])
print(carros[1])

#Métodos:

carros2 = list(carros) #Ao utilizando essa lógica com o casting, seria como se estivéssimos criando uma nova list, pois se colocarmos uma list dentro de outra variável e fizermos alguma operação com algum método na variável que contém a primeira list, isso influencia também a primeira list.

carros2.append('Fusion') #O método append serve para acrescentar mais um tipo de dados dentro de uma list.

carros2.remove('HRV') #Neste método, usamos para remover algum índice da list.

carros2.pop() #Esse método remove o último elemento da nossa list.

del carros2[0] #Esse é mais um modo de remover um índice da list.

#carros.clear() Com o método clear, ele limpa toda a list.

carros2[0] = 'Mobi' #Aqui observamos que o list é algo indexável, ou seja, posso usar a indexação com o índice para gerenciar ou retornar outro valor no elemento da list.

info = carros + pecas #E assim dessa forma, juntamos uma list com outra.

print(str(len(carros)) + ' índices na primeira list.')#Esse método serve para sabermos quantos índices temos dentro de uma list.
print(str(len(carros2)) + ' índices na segunda list.')

print(carros)
print(carros2)
print(info)

#