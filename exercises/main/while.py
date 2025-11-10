frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

#A barra invertida é somente pra que eu possa quebrar a linha no código.

#print(frase.count('a'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qts_vezes_str_aparece = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qts_vezes_str_aparece:
        qtd_apareceu_mais_vezes = qts_vezes_str_aparece
        letra_que_apareceu_mais_vezes = letra_atual

    print(letra_atual, qts_vezes_str_aparece)
    i += 1