import sys
import os

caminho = r'C:\Users\Elisangela\Documents\Python\exercises\others'
sys.path.append(caminho)

print("Pasta adicionada ao sys.path:", caminho)
print("Arquivos na pasta:", os.listdir(caminho))

try:
    import module_python
    print("Módulo importado com sucesso!")
except ModuleNotFoundError:
    print("Módulo NÃO encontrado! Verifique nome e extensão do arquivo.")

import modularization_main #E assim podemos importar nossa própria biblioteca.
#Mas pra isso, precisamos que o arquivo esteja na mesma pasta.
#Quando não especificamos algum módulo no nosso código, sempre o primeiro a executar no python é o __main__ através do name.

print('Este módulo se chama:', __name__)
print(*sys.path, sep='\n')