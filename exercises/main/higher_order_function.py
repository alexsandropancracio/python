def mensagem(msg, *nome):
        return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(mensagem, 'Bom dia', 'Luis')
)