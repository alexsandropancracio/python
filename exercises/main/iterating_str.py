iterador = 'Alexsandro'

iterando = 0
nova_palavra = ''

while iterando < len(iterador):
        letra = iterador[iterando]
        nova_palavra += f'*{letra}'
        iterando += 1

nova_palavra += '*'
print(nova_palavra)