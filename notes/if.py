#Basicamente o if é um comando de descisão com um teste lógico como true ou false, que cada condição executa um bloco de comandos.

x = True

if x:
    print('Hello world!')#O resultado desse programa, se a expressão retornar True, ele executa um bloco de comando para o condicional True, senão, ele não executa o bloco de comando e sai executando assim a próxima expressão. Dando a entender que o "if" executa algo que é True.

y = 10
z = 5
res = 0
w = '+'

if y > z:
    print('Sim, y é maior do que z.')

if w == '+':
    res = y + z
elif w == '-':
    res = y - z
elif w == '*':
    res = y * z
elif w == '/':
    res = y / z
else:
    print('Operador inválido.') 

#A grande desvantagem disso é, um programa muito grande com muitos "if", o desemprenho do programa fica prejudicado, principalmente se for um dispositivo com o poder de processamento menor. Pra melhorar esse desemprenho de processamento nós usamos o "else if". Mas no caso do Python, ele tem uma diferente referente às outras linguagens de programação, o "else if" funciona no python como "elif". Usando "elif", ele sai da estrutura "if" e não testa "if" por "if".

print('Sim, a operação é ' + w + ':', res)#Percebemos que com o uso da vírgula, não identificamos o "TypeError: can only concatenate str (not "int") to str", ou seja, sim, ela separa argumentos que serão impressos no console, pois a vírgula ela separa qualquer tipo de dado, mas ela antes sempre acrescenta um espaço por padrão.

#A diferença de concatenar usando o "+", ele por obrigatoriedade, exige que todos os elementos sejam strings.

#Mas pra melhor uso disso, de forma mais elegante e coesa, usamos o f-string.

#Além de percebermos que "w" é diferente de "+"" na condicional "if", ele não executa a operação do bloco da condição e mostra o valor que a variável "res" tem por padrão. Ou seja, "res" foi inicializado em 0 e não foi alterado além de que o print foi executado, por estar fora do bloco de código da condicional "if", caso contrário, teríamos um "TypeError!".

print(str(y), w, str(z), '=', str(res))

clima = 'chuva'
dinheiro = 300
lugar = ''

if clima == 'sol' and (dinheiro >= 200 and dinheiro <= 500): #Aqui compomos o teste lógico com o operador "or" ou "and".
    lugar = 'sair'
else:
    lugar = 'ficar em casa'

print('De acordo com o clima e com o dinheiro que eu tenho, eu vou ' + lugar + ".")

print('Fim do programa.')

