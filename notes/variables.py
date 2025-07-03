num = res = 0
curso = "Python"

def assunto():
    print(curso)

assunto()

def bonus():
    global var #Sempre quando inicializamos uma variável com escopo global, nunca pode haver na mesma linha o que irá armazenar na variável.
    var = 'Assim determinaos uma variável de escopo global.'
bonus()#Pra funcionar a chamada da variável global, devemos chamar a função.

print(var)