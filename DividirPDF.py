import PyPDF2

def dividir_pdf(caminho_pdf, pasta_saida):
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor = PyPDF2.PdfFileReader(arquivo_pdf)
        
        for pagina_num in range(leitor.numPages):
            escritor = PyPDF2.PdfFileWriter()
            escritor.addPage(leitor.getPage(pagina_num))
            
            nome_saida = f"{pasta_saida}/pagina_{pagina_num + 1}.pdf"
            with open(nome_saida, 'wb') as arquivo_saida:
                escritor.write(arquivo_saida)

# Exemplo de uso
caminho_pdf = 'informe.pdf'
pasta_saida = 'saida'
dividir_pdf(caminho_pdf, pasta_saida)