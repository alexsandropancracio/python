import time

def linha():
    print('-' * 50)

def sacar():
    saldo = 500  # acesso ao banco de dados
    limite = 500
    sacou = 0
    saques = 0
    depositou = 0

    while True:
        time.sleep(1)
        operar = input('Pressione Enter para acessar sua conta. \n')
        enter = ""

        if operar == enter:
            #login = input('Login: ').strip()
            #senha = input('Senha: ').strip()
            time.sleep(0.8)
            print('Aguarde um momento, estamos processando...\n')
            time.sleep(3)
            print('Olá, seja bem vindo/a!')
            time.sleep(1)

            while True:
                linha()
                print('Saldo atual: R${:.2f}'.format(saldo))
                opcao = int(input('Informe uma opção: \n[1]Saque\n[2]Deposito\n[3]Extrato\n[0]Sair\nOpção: '))
                linha()
                opcoes = [0, 1, 2, 3]

                if opcao == 1:
                    while True:
                        if saques <= 1:
                            total = input('Valor: R$')
                            saques += 1

                            if total == "":
                                print('Valor inválido. Por favor, tente novamente.\n')
                                time.sleep(1)

                            else:
                                total = float(total)

                                if total <= saldo and total <= 500 and total >= 0:
                                    print('Analisando saldo...')
                                    time.sleep(2)
                                    print('Valor aprovado.')
                                    time.sleep(1)
                                    print('Retire o seu dinheiro na boca do caixa.')
                                    time.sleep(2)
                                    print('Obrigado pela preferência. Volte sempre!\n')
                                    time.sleep(2)
                                    saldo -= total
                                    sacou += total


                                elif total > 500:
                                    print(f'Seu saque ultrapassa o saldo limite de R${limite:.2f}, tente novamente.\n')
                                    time.sleep(1)

                                elif total > saldo:
                                    print('Analisando saldo...')
                                    time.sleep(2)
                                    print(f'Seu saldo é de R$ {float(saldo)} e você deseja sacar R$ {float(total)}')
                                    time.sleep(1)
                                    tente = input('Saldo insuficiente. Deseja transferir algum valor pra sua conta? Sim/Não \n').lower()

                                    if tente == "sim":
                                        transferir = int(input('Valor a ser transferido: '))
                                        saldo += transferir
                                        print('Transferindo o valor...')
                                        time.sleep(3)
                                        print('Valor transferido com sucesso.\n')
                                        time.sleep(2)
                                        break

                                    elif tente == "não":
                                        print('Fim de transação. \n')
                                        time.sleep(2)
                                        break

                                    if total == enter:
                                        print('Informação inválida. Por favor, tente novamente.\n')
                                        time.sleep(1)
                                break

                        else:
                            print('''Você atingiu o limite de saque diário.
Por favor, volte amanhã para mais saques ou entre em contato com nossa central.''')
                            print('')
                            time.sleep(1)
                    break

                if opcao == 2:

                    deposito = float(input('Valor: R$'))

                    while True:
                        if deposito >= 1:
                            saldo += deposito
                            depositou += deposito
                            time.sleep(1)
                            print('Aguarde um momento, estamos operando a transação.')
                            time.sleep(3)
                            print('Deposito efetuado com sucesso!')
                            time.sleep(2)
                            novo_deposito = input('Deseja efetuar um novo depósito? Sim/Não\n')
                            if novo_deposito == "sim":
                                time.sleep(1)
                                continue
                            elif novo_deposito == "não":
                                print('Obrigado pela preferência. Volte sempre!\n')
                                time.sleep(2)
                                break

                        else:
                            print('Informação inválida. Por favor, tente novamente!\n')
                            time.sleep(1)
                    break

                if opcao == 3:

                    while True:
                        time.sleep(1)
                        print('Processando extrato...')
                        time.sleep(2)
                        print('Extrato processado: ')
                        linha()
                        print('''
Seu total de operações hoje:
-Depositou: R${:.2f}
-Sacou: R${:.2f}
                        '''.format(depositou, sacou))
                        linha()
                        voltar = input('Aperte Enter para voltar às opções anteriores.\n')

                        if voltar == "":
                            print('Operação concluída!')
                            time.sleep(2)
                            break
                    continue
                if opcao == 0:

                    print('Obrigado pela preferência. Volte sempre!\n')
                    time.sleep(2)
                    break

                if opcao != opcoes:
                    print('Informação inválida. Tente novamente.')
                    time.sleep(1)

sacar()