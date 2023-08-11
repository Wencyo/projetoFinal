import requests
import os


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
            analise_resposta()
            


    