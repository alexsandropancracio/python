s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Alex',1,2,3))
s1.discard('Luiz')
#print(s1)

# Operadores Úteis:
# união | (union) - Une
# intersecção & (intersection) - Mostra somente itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s2 = {1,2,3}
s3 = {2,3,4}
s4 = s2 | s3
s4 = s2 & s3
s4 = s2 - s3
s4 = s2 ^ s3

letras = set()
while True:
    digitou = input('Digite: ')
    letras.add(digitou)
    print(letras)