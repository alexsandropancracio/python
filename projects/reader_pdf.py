from PyPDF2 import PdfReader

caminho_pdf = r"C:\Users\Alex\Documents\exe\empresa\Cadastro Nacional de Muturios - CONSULTA CONTRATO.pdf"
reader = PdfReader(caminho_pdf)
page = reader.pages[0]
print(page.extract_text())
