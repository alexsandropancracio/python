from sys import exit, platform#Nesse módulo, importamos funções do sys, então não precisamos usar sys.exit()
#from sys import * #isso aqui chamamos de má prática, que é onde tudo sys, mas fica meio obscuro pois não há nada definido, ou seja, eu posso sobrescrever a variável do módulo sem saber.

#platform = 'TESTE' evite isso, pois pode sobrescrever a biblioteca.

print(platform)
#exit()