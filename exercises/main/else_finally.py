try:
    print('ABRIR ARQUIVO')
    8/0 
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
    print('DIVIDIU POR ZERO')#Se eu finalizar aqui, ele não vai finalizar a excessão do erro.
else:
    print('NÃO DEU ERRO')#Caso o try funcione, o codigo executa em seguida o else.
finally:
    print('FECHOU ARQUIVO')#Se percebermos, o código é todo executado mas se der erro, executa da mesma forma e vai direto pro finally. Tipo, ocorreu ou não ocorreu o erro, o finally vai ser executado ocorra o que ocorrer.