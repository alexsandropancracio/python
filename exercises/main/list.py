import os
import time

lista = []

while True:
    try:
        os.system('cls')
        opcao = int(input('[1]Listar \n[2]Adicionar \n[3]Apagar \n\nSelecione uma opção: '))
        selecionado = opcao - 1
        if selecionado == 0:
            while True:
                if len(lista) == 0:
                    print('\nLista vazia. Preencha para visualizar os itens.')
                    time.sleep(2)
                    break
                else: 
                    os.system('cls')
                    for indice, itens in enumerate(lista):
                        print(f'{indice} - {itens}')
                    saindo = input('\nPressione Enter para sair: ')
                    if saindo == '':
                        break
                    else:
                        print('Digite a opção correta para sair.')
                        time.sleep(2)
        if selecionado == 1:
            while True:
                if lista:
                    os.system('cls')
                    for indice, itens in enumerate(lista):
                        print(f'{indice} - {itens}')
                    listando = input('\nEscreva o que quer para adicionar na lista ou pressione Enter para sair: ')         
                    if listando == '':
                        break
                    
                    lista.append(listando)
                else:
                    os.system('cls')
                    listando = input('Escreva o que quer para adicionar na lista ou pressione Enter para sair: ')         
                    if listando == '':
                        lista.pop(listando)
                        break
                    lista.append(listando)
        if selecionado == 2:
            if len(lista) == 0:
                print('\nLista vazia. Preencha para remover algum itens.')
                time.sleep(2.5)       
            else:
                while True:
                    os.system('cls')
                    for indice, itens in enumerate(lista):
                        print(f'{indice} - {itens}')
                    try:
                        removendo = input('\nDigite um número de acordo com o índice para remover ou pressione Enter para sair: ')
                        if removendo == '':
                                break
                        if removendo < len(lista):
                            if removendo >= 0:
                                removido = int(removendo)                        
                                lista.pop(removido)                                        
                    except:
                        print('\nDigite somente números de acordo com as opções. Tente novamente!')
                        time.sleep(3)
    except:
        print('\nDigite somente números de acordo com as opções. Tente novamente!')
        time.sleep(3)
        continue