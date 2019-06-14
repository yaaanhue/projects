#!/usr/bin/python3
#Info in Files - Scraper informations in files: .txt
#Writed by Yan Luiz - git: https://github.com/yaaanhue

import os, pprint

infosFound = []         #lista com o nome dos arquivos de texto e para todas as informacoes encontradas nos arquivos
contactsList = {}       #dicionarios para salvar os numeros que foram encontrados no meio dos dados

#recebe um diretorio e verifica se ha outros diretorios dentro, e se dentro desses ou do principal ha arquivos de texto
def verifyDir(directory):
        #muda o diretorio de trabalho para o diretorio que foi passado para a funcao
    os.chdir(directory)
    for filesinDir in os.listdir('.'):
        #se for uma pasta entra e le todos os txt dentro dela (nesse caso eu sei que so tem txt dentro dela)
        if os.path.isdir(filesinDir) == True:
            os.chdir(filesinDir)
            for txtFile in os.listdir('.'):
                    #adiciona um indice na lista com o nome do arquivo
                    infosFound.append(txtFile)
                    textFile = open(txtFile)
                    #le o arquivo e salva todas as strings de texto no indice seguinte da lista
                    infosFound.append(textFile.readlines())
                  
#recebe uma lista de strings e verifica se ha numeros nela
def findNumbers(listStrings):
        #cria uma lista temporaria para armazenar os numeros que encontra
        numbers = []
        #fara uma interacao por cada string da lista de strings passando por toda ela
        for size in range(len(listStrings)):
                #verifica se ha caracteres na string, se houver ira salvar na variavel auxiliar numbersFound
                numbersFound = ''.join(filter(str.isdigit, listStrings[size]))
                #ira salvar na lista apenas o grupo de numeros com pelo menos 8 caracteres
                if len(numbersFound) > 8:
                        numbers.append(numbersFound)
                else:
                        continue
        #retorna a lista de numeros encontrados para depois ser armazenado no dicionario
        return numbers

#passa meu diretorio atual para a funcao que verifica e le os arquivos de texto
verifyDir(os.getcwd())

for i in range(0,len(infosFound),2):
        #criara no dicionario chaves com o nome do arquivo e passara as strings de conteudo para uma funcao trata essas strings e extrai os numeros
        contactsList.setdefault(infosFound[i],findNumbers(infosFound[i+1]))
        #faz um print elegante (linha por linha) do conteudo do dicionario, nomes e numeros

pprint.pprint(contactsList)

