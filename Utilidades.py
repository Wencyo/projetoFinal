import requests
import os

import Entidades
import Filtros
import os
import time
from urllib.parse import urlparse

class Tratamento_Resposta:
    def __init__(self, resposta):
        self.resposta = resposta

    #Funções para cada grupo de codigos
    def Informativo(self):
        print("Recebemos sua informação e estamos processando-a:", self.resposta.status_code)

    def Sucesso(self):
        print("Requisição Bem-sucedida!:", self.resposta.status_code)

    def Redirecionamento(self):
        print("Temporariamente ou permanentemente localizado em outro lugar!", self.resposta.status_code)

    def Cliente_erro(self):
        print("Problema de Conexão: Erro do cliente.", self.resposta.status_code)

    def Servidor_erro(self):
        print("Problema de Conexão: Erro no servidor interno.", self.resposta.status_code)

    #Analisando a resposta de requisição
    def analise_resposta(self):
        codigo = self.resposta.status_code
        indice = str(codigo)[0]

        if indice == '1':
            self.Informativo()
        elif indice == '2':
            self.Sucesso()
        elif indice == '3':
            self.Redirecionamento()
        elif indice == '4':
            self.Cliente_erro()
        elif indice == '5':
            self.Servidor_erro()
        else:
            print("Codigo de status desconhecido:", codigo)

    #Impressão do conteudo da resposta    
    def Cabeçalho_Conteudo(self):
        if self.resposta.status_code == 200:
            head = self.resposta.headers
            print("Cabeçalhos:", head)

            conteudo = self.resposta.json()
            print("Conteúdo:", conteudo)
        else:
            self.analise_resposta()

class local_ou_Publica:
    def imagem_publica(self, url):
        try:
            resposta = requests.head(url)
            return resposta.status_code == 200
        except requests.RequestException:
            return False
    
    def imagem_local(self, caminho):
        return not urlparse(caminho).scheme

class Util:
    def extrair_nome_extensao_url(self, url):
        parsed_url = urlparse(url)
        caminho_arquivo = parsed_url.path
        nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
        return nome_arquivo, extensao

    def wait_for_file(self, caminho, intervalo=1):
        print('Aguarde...')
        while not os.path.exists(caminho):
            time.sleep(intervalo)
            intervalo = intervalo + 1
            print(".", end=" ")

class Main:
    def __init__(self, utilidades):
        self.utilidades = utilidades

    def cria_imagem(self, minha_url):
        try:
            print(f'URL: {minha_url}')
            nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
            arquivo = nome_arquivo + extensao_arquivo
            print(f'Arquivo: {arquivo}')
            meu_download = entidades.Download(url=minha_url, path_arquivo=arquivo)
            print(f'Inicia download...')
            if meu_download.download_file():
                print(f'Download concluído!')
            else:
                print('Erro durante o download!')

            # Para reproduzir a imagem
            imagem = Entidades.Imagem(id=1, nome_arquivo=arquivo, path_arquivo=arquivo)
            print(imagem)
            return imagem.conteudo()
        except Exception as ex:
            print(f'Erro ao criar imagem: {str(ex)}')

    def aplica_filtro(self, minha_imagem, nome, extensao, filtro):
        try:
            print('Aplicando filtro')
            # Aplicar o filtro
            imagem = filtro.apply_filter(minha_imagem)
            # Salvar a imagem
            nome = nome + '_imagem.' + extensao
            imagem.save(nome)
            print(f'Filtro grayscale aplicado com sucesso! Arquivo salvo em {nome}')
        except Exception as ex:
            print(f'Erro ao aplicar filtro: {str(ex)}')

    def listar_conteudo(self):
        diretorio = "."
        files = os.listdir(diretorio)
        jpeg_files = [file for file in files if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg")]
        png_files = [file for file in files if file.lower().endswith(".png")]
        lista_imagens = jpeg_files + png_files

        return lista_imagens


    