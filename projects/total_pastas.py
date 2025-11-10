import os

pasta_raiz = r"C:\Users\Alex\Documents\exe"
pastas = [p for p in os.listdir(pasta_raiz) if os.path.isdir(os.path.join(pasta_raiz, p))]
print(f"Total de pastas atuais {len(pastas)}")