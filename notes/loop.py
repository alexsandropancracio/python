#Em python só temos dois loop, que é o for e o while. Mas agora, vamos aprender sobre o loop for.

carros = ['HRV', 'Golf', 'Argo', 'Focus']

print(carros)

for x in carros:
    print(x)
    if (x == 'Golf'):
        print('Sim, a variável "x" é igual a Golf')
#Como funciona o loop for? Eu crio uma variável pra receber os elementos de uma coleção e informo qual coleção eu quero percorrer, percorrendo assim cada elemento da coleção, ele adiciona na variável "x" criada no "for" e assim sucessimavente imprimindo no console cada tipo de dado.

for y in ['Python', 'Java', 'C#', 'C++', 'Kotlin']:
    print(y) #A diferença aqui é que não tenho uma lista criada dentro de uma variável, então posso colocar ela no escopo do "for".

for x in carros:
    print(x)
    if (x == "Argo"):
        break #Aqui determinamos com uma condição até onde o loop pode percorrer, encerrando ele com o "break".

print('Fim do programa.')