x = 1 #int
x = "Python" #string
x = 10.0 #float
x = False #bool
num = 2; img = 3; x = complex(num, img)
w = ["abc", "def", 1.5, 10, True] #list / array Além disso, aqui podemos armazenar tipos de dados diferentes.
y = ("Alex", 28, False) #tuple
z = { 
    "Nome": "Alex",
    "Idade": "28"
} #dict
order = {1, 2, "alex", 10.0, True, 2, "2"} #set O set é algo que remove tipo de dados iguais.

print(x.real)
print(x.imag)
print(x)
print(type(x))

print('Valor: ' + str(x))
print('Tipo de Dados: ' + str(type(x)))#para que houvesse a impressão dos dados, foi necessário fazermos a corversão de casting.

w[0] = "yxz"
print(w[0])
print(y)
print(y[1])
print(z["Nome"])
print(type(z))
print(order)