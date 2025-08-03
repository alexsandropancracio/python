#O loop while ele precisa de uma condição pra informar se ele vai continuar sendo executado ou não.

#A sintaxe é bastante simples:

'''inicialozação de variável de controle
while (teste lógico)
    comandos
    enquanto o teste retornar True ele executa os comandos
    incremento, decremento ou controle'''

#Devemos ter muito o controle do teste lógico para não termos um loop infinito.

import os

carros = ['HRV', 'Golf', 'Argo', 'Onix']
index = 0
total = 0
tamanho = len(carros)

while total < tamanho:
    print(carros[total])
    total += 1

while  index < 9:
    print(index)
    index += 1
    if index == 5:
        break
print('\nFim do loop!')#\n Serve para quebrar uma linha.

motos = []
init = input('Pressione enter para começar o programa.')
while True:
    moto = input('Digite a marca de uma moto(Finalizar: y/n): ')
    motos.append(moto)
    if moto == 'y':
        motos.remove('y')
        break
    elif moto == 'n':
        continue

os.system('cls')#Limpa a tela do terminal.


print('As marcas das motos escolhidas são: ')
for x in motos:
    print(x)
