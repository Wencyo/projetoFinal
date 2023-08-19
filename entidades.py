from PIL import Image
import requests
import os
from tkinter import Tk, filedialog

#Classes do Projeto:
#Classe para fazer o Download da Imagem
class Download:
    def __init__(self, url, destino_arquivo):
        self.url = url
        self.destino_arquivo= destino_arquivo

    def download_file(self):
        try:
            resposta = requests.get(self.url)
            resposta.raise_for_status() 
            with open(self.destino_arquivo, "wb") as file:
                file.write(resposta.content)
                return True
            # print(f"Download Completo. Arquivo Salvo Em : {self.destino_arquivo}")
        
        except requests.exceptions.MissingSchema:
            print("URL Inválida. Certifique-se de fornecer uma URL válida.")
            return False
        except requests.exceptions.RequestException as e:
            print(f"Erro na Conexão: {e}")
            return False

# Classe para representar um arquivo de imagem, .jpg ou .png
class Imagem:
    imagem = None

    def __init__(self, id, nome_arquivo, destino_arquivo):
        self.id = id
        self.nome_arquivo = nome_arquivo
        self.local_referencia = destino_arquivo
        try:
            self.imagem = Image.open(destino_arquivo)
        except Exception as ex:
            print(f"Erro ao criar imagem com o arquivo {nome_arquivo} na referência {destino_arquivo}: {str(str)}")

    def dimensoes(self):
        return self.imagem.size
    
    def tamanho(self):
        return os.path.getsize(self.local_referencia)

    def formato(self):
        return self.imagem.format
    
    def conteudo(self):
        return self.imagem
    
    def __str__(self):
        return f"Nome: {self.nome_arquivo}, Dimensões: {self.dimensoes}, Formato: {self.formato()}, Tamanho: {self.tamanho()} Bytes"
