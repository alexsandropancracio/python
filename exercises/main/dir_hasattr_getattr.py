#O dir faz a gente ver no debug console quais métodos existem pra o tipo de dado.
#hasattr faz a gente verificar isso no terminal, sem precisar ir pro debug.
#getattr 

string = 'Alex'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper.')
    print(getattr(string, metodo)())#Assim verificamos manualmente o método de um tipo de dado.
else:
    print('Não existe o método', metodo)