import os
import time

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': [1,3,4,7],
        'Resposta': 4
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': [25,55,10,51],
        'Resposta': 25
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': [6,3,5,9],
        'Resposta': 5
    }
]

while True:
    erros = 0
    acertos = 0
    encerrou = False
    for pergunta in perguntas:
        while True:
            print(f'Pergunta: {pergunta['Pergunta']}')
            print()
        
            for i, opcao in enumerate(pergunta['Opções']):
                print(f'{i}) {opcao}')        
            print()       

            try:
                resposta = int(input('Escolha a alternativa certa: '))
                if resposta >= 0 and resposta < len(pergunta['Opções']):
                    respondeu = pergunta['Opções'][resposta]
                    if respondeu == pergunta['Resposta']:
                        print('Acertou!\n')
                        acertos += 1
                    else:
                        print('Errou.\n')
                        erros += 1
                    break        
                else:
                    print('Opção não existe. Por favor, tente novamente.\n')
            except ValueError:
                print('Por favor, digite somente números de acordo com as opções.\n')

                
    if acertos > 2:
        print('Parabens, você ganhou!')
        print(f'Acertos: {acertos}')
        print(f'Erros: {erros}')
    else:
        print('Você perdeu. Tente novamente.')
        print(f'Acertos: {acertos}')
        print(f'Erros: {erros}')

    while True:
        saida = input('Deseja jogar novamente? (y/n): ')
        if saida == 'y':
            break     
        elif saida == 'n':   
            print('Obrigado, volte sempre!')
            encerrou = True
            break     
        else:
            print('Opção inválida. Tente novamente.')
    if encerrou:
        break
                    