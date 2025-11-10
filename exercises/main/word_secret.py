palavra = 'python'
tentativas = 0
acertadas = ''

while True:   
        letra = input('Digite uma letra: ')
        
        if len(letra) > 1 or letra == '' or not letra.isalpha():
            print('Digite somente uma letra.')
            continue
 
        if letra in palavra:
            acertadas += letra
        else:
            tentativas += 1

        palavra_secreta = ''
        for letra_secreta in palavra:
            if letra_secreta in acertadas:
                 palavra_secreta += letra_secreta
            else:
                 palavra_secreta += '*'
        
        print('Palavra secreta: ', palavra_secreta)

        if palavra_secreta == palavra:
             print('Parabéns, você completou o jogo!')
             print(f'A palavra secreta é: "{palavra_secreta}" \nE para acertar você tentou por {tentativas} vezes.')
             break