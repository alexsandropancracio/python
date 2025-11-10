def criar_saudacao(saudacao, nome):
    def saudando():
        return f'{saudacao}, {nome}!'
    return saudando

cumprimentos = criar_saudacao("Bom dia", "Alex")

print(cumprimentos())#Isso chamamos de closure.