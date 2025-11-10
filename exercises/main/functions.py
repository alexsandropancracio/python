def soma(x, y=None, z=None):#Todo o parâmetro que for nomeados com argumento padrão, todos os restantes devem ter o valor padrão também.
    if z is not None:
        print(f'{x = } + {y = } + {z = } | x + y + z = {x+y+z}')
    else:
        print(f'{x = } + {y = } | x + y = {x+y}')

#soma(1,y=2,3)Toda vez que eu nomear um parâmetro, eu tenho que nomear os parâmetros restantes também, senão dá erro de Syntax. Geralmente eu uso parâmetros nomeados caso eu queira mudar a ordem deles pra adicionar e mostrar os argumêntos. Ex:

#soma(z=1, y=2, x=3)

soma(1,2,3)

#Mas podemos nomear um parâmetro na função caso queira um valor padrão.

x = 1

def escopo():
    global x
    x = 10

    def outro_escopo():#Aqui entendemos que as variáveis dentro do escopo não podem ser usadas pro escopo antrior.
        global x #Aqui eu defino que a variável "x" é global desse escopo, pois se houvesse o "x" como global no escopo anterior, o resultado de "x" seria global somente desse escopo.
        x = 11
        y = 2
        print(x, y)
    
    outro_escopo()
    print(x)

print(x)
escopo()
print(x)