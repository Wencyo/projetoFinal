import entidades
import filtros
import utilidades
import os
from tkinter import *
from tkinter import Tk, filedialog

class Principal:
    def menu(self):
        print("---------------- MENU ----------------")
        print("1. Informar o caminho da imagem")
        print("2. Aplicar filtro na imagem")
        print("3. Listar arquivos de imagem do diretório atual")
        print("4. Sair")

    def menu_filtros(self):
        print("\nEscolha um filtro para ser aplicado:")
        print("1. Escala de Cinza")
        print("2. Preto e Branco")
        print("3. Cartoon")
        print("4. Negativo")
        print("5. Contorno")
        print("6. Blurred")
        
    def menu_entrada(self):
        print("\nEscolha uma como a imagem vai ser obtida :")
        print("1. URL")
        print("2. Imagem local")
        
    def excutar(self):
        utilidades1 = utilidades.Util()
        app_principal = utilidades.Main(utilidades1)
        escolhas = Principal()
        
        while True:
            opcao = 0
            while (opcao < 1 or opcao > 4):
                escolhas.menu()
                try:
                    opcao = int(input("Selecione uma opção(1-4): "))
                except ValueError as e:
                    print("Ocirreu um erro:", str(e))

            if opcao == 1:
                
                opcao_entrada = 0
                while (opcao_entrada < 1 or opcao_entrada > 2):
                    try:
                        escolhas.menu_entrada()
                        opcao_entrada = int(input("Selecione uma das opçoes (1-2): "))
                    except ValueError as e:
                        print("Ocirreu um erro:", str(e))   
                                                
                if opcao_entrada == 1:
                    caminho_imagem = input("\nInforme o caminho da imagem(URL): ")
                    nome_imagem = input("Informe o nome da imagem: ")

                    imagem1, extensao  = app_principal.cria_imagem(caminho_imagem)
                                        
                elif opcao_entrada == 2:

                    print("A pagina para selecionar deve estar aberta")
                    filename = utilidades1.selecionar_imagem_local()
                    
                    imagem1, extensao  = app_principal.cria_imagem2(filename)
                    
                    nome_imagem = input("Informe o nome da imagem: ")     
                             
            elif opcao == 2:
                if imagem1:
                    
                    opcao_filtro = 0
                    while (opcao_filtro < 1 or opcao_filtro > 6):
                        try:
                            escolhas.menu_filtros()
                            opcao_filtro = int(input("Selecione um filtro (1-6): "))
                        except ValueError as e:
                            print("Ocirreu um erro:", str(e))
                    
                    if opcao_filtro == 1:
                        app_principal.aplica_filtro_escala_de_cinza(imagem1, nome_imagem, extensao)
                    elif opcao_filtro == 2:
                        app_principal.aplica_filtro_preto_e_branco(imagem1, nome_imagem, extensao)
                    elif opcao_filtro == 3:
                        app_principal.aplica_filtro_cartoon(imagem1, nome_imagem, extensao)
                    elif opcao_filtro == 4:
                        app_principal.aplica_filtro_negativo(imagem1, nome_imagem, extensao)
                    elif opcao_filtro == 5:
                        app_principal.aplica_filtro_contorno(imagem1, nome_imagem, extensao)
                    elif opcao_filtro == 6:
                        app_principal.aplica_filtro_blurred(imagem1, nome_imagem, extensao)
                    else:
                        print("Opção Inválida.")
                else:
                    print("Irfome o caminho da imagem antes de escolher o filtro.")
            
            elif opcao == 3:
                for elemento in app_principal.listar_conteudo():
                    print(elemento)
            elif opcao == 4:
                print("Aguarde...")
                app_principal.apagar_imagens(app_principal.listar_conteudo())
                print("Programa Encerrado.")
                break
            else:
                print("Opção Inválida.")

aplicacao = Principal()
aplicacao.excutar()