import sys

#Generator expression, Iterables e Iterators em Python
iterables = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterables) #tem .__iter__ e .__next__
lista = [n for n in range(10000)]#Isso daqui está tudo na memória do computador.
generator = (n for n in range(100000))#Pra que tudo isso vá para a memória do computador, eu uso o for.
#Ou seja, com o generator a gente tem menos processamento de dados na memória do hardware.


print(sys.getsizeof(lista))#podemos ver o tamanho do objeto.
print(sys.getsizeof(generator))

print(next(generator))

#print(next(iterator))#Aqui percebemos que ele não conhece o tamanho do objeto.

