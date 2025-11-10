
n1 = 10
n2 = 5

def somar():
    r = n1 + n2
    print(r)


def subtrair():
    r = n1 - n2
    print(r)

def multiplicar():
    r = n1 * n2
    print(r)

def calculos():
    somar()
    subtrair()
    multiplicar()

calculos() #Aqui entendemos que estamos chamando funções com outra função.

#Argumentos de Entrada/Parâmetros

def somar(n1, n2):#Pra almentar a soma dos valores eu uso mais parâmetros como: def somar(n1, n2, n3, n4)
    r = n1 + n2
    print(f'{n1} + {n2} = {r}')

#Argumentos Arbitrários é o tipo de parâmetro onde podemos ter diversos valores ao invés de especificar por variáveis como mostra acima.

palavras = ['Dia', 'Noite', 'Acordar', 'Dormir']


def textos(txt): #Aqui notamos que pra uma lista usamos um parâmetro só de entrada, sem necessidade de arbitrariedade.
    for res in txt:
        print(res)

def subtrair(*num):
    r= num[0] #Primeiro valor.
    for x in num[1:]: #Do segundo em diante.
        r -= x
    print(r)

subtrair(5, 4)

def carros(c = 'Mercedez'): #Argumento com valor padrão.
    print('Modelo: ' + c)

carros('BMW')
carros()

textos(palavras)

valores = [1, 3, 5, 4]

def multiplicando(total):
    r = total[0]
    for y in total[1:]:
        r *= y
    return r

def val(res):
    for x in res:
        print(x, end=', ')

print(str(val(valores)) + " multiplicando um por um dá o total de: " + str(multiplicando(valores)))


#funções lambda

#lambda argumento: expressao #expressão simples e anônima, não preciso me preocupar com o return

soma = lambda a,b: a+b

resultado = soma(2,5)

print(resultado)
print(soma(2,5))

mult = lambda a,b,c: (a+b)*c

print(mult(2,5,3))

print((lambda a,b: a-b)(3,2))

fun = lambda x,func: x+func(x)
res = fun(2, lambda y: y*y)#passei o valor 2 para x, para func eu passei o valor de x para a lambda y(=2): y(=2)*y(=2)= 4. O func(x) é igual o  lamb

print(res)
res = fun(3, lambda z: z+4)
print(res)