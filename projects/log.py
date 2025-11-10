import os
from unidecode import unidecode

# Caminho da pasta onde estão as subpastas
pasta_raiz = r"C:\Users\Alex\Documents\PROJECTS\PASTAS VAZIAS\PASTAS VAZIAS"
caminho_log = os.path.join(pasta_raiz, "pastas_listadas.txt")

# Garante que o nome será tratado corretamente mesmo se vier com caracteres bugados
def corrigir_nome(nome):
    try:
        # Tenta decodificar e reformatar (simula correção de codificação errada)
        nome_corrigido = nome.encode('latin1').decode('utf-8')
    except:
        nome_corrigido = nome  # se der erro, usa o original mesmo
    
    nome_formatado = unidecode(nome_corrigido).replace("_", " ")
    return nome_formatado

# Cria o arquivo txt com os nomes corrigidos
with open(caminho_log, "w", encoding="utf-8") as arquivo:
    for nome in os.listdir(pasta_raiz):
        caminho_completo = os.path.join(pasta_raiz, nome)
        if os.path.isdir(caminho_completo):
            nome_tratado = corrigir_nome(nome)
            arquivo.write(f"{nome_tratado}\n")

print(f"✅ Lista com nomes corrigidos salva em: {caminho_log}")
