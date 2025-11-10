import re
import sys

cpf_usuario = '860.396.585-41'
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    cpf_usuario
)
nove = cpf_enviado[:9]
primeiro = 10

entrada_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

resultado_primeiro = 0
resultado_segundo = 0

for digito in nove:
    multiplicando = int(digito) * primeiro   
    #print(multiplicando) 
    primeiro -= 1
    resultado_primeiro += multiplicando

digito_calculo1 = (resultado_primeiro * 10) % 11
digito1 = digito_calculo1 if digito_calculo1 <= 9 else 0
#print(f'O valor do primeiro dígito é: {digito1}\n')

dez = nove + str(digito1)
segundo = 11

for digito in dez:
    multiplicando = int(digito) * segundo
    #print(multiplicando)    
    segundo -= 1
    resultado_segundo += multiplicando

digito_calculo2 = (resultado_segundo * 10) % 11
digito2 = digito_calculo2 if digito_calculo2 <= 9 else 0
#print(f'O valor do segundo dígito é: {digito2}')

cpf_calculo = f'{nove}{digito1}{digito2}'

if cpf_enviado == cpf_calculo:
    print(f'O CPF {cpf_enviado} é válido')
else:
    print(f'O CPF {cpf_enviado} é inválido.')