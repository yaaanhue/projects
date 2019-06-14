#!/usr/bin/python3
#Info in Files - Scraper informations in files: .txt
#Writed by Yan Luiz - git: https://github.com/yaaanhue

import os, pprint, re

infosFound = []         #1 Tratamento de dados - lista com o nome dos arquivos de texto e para todas as informacoes encontradas nos arquivos
allNumbersFound = {}       #2 Tratamento de dados - dicionarios para salvar os numeros que foram encontrados no meio dos dados

listIndices = []        #lista de indices onde nao encontrou numeros
celNumbersFound = {}    #dicionario para os numeros de celular encontrados

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
def findAllNumbers(listStrings):
        #cria uma lista temporaria para armazenar os numeros que encontra
        numbers = []
        #fara uma interacao por cada string da lista de strings passando por toda ela
        for size in range(len(listStrings)):
                #verifica se ha numeros na string, se houver ira salvar na variavel auxiliar tempNum
                tempNum = ''.join(filter(str.isdigit, listStrings[size]))
                #ira salvar na lista apenas o grupo de numeros com pelo menos 8 caracteres
                if len(tempNum) > 8:
                        numbers.append(tempNum)
                else:
                        continue
        #retorna a lista de numeros encontrados para depois ser armazenado no dicionario
        return numbers

#recebe strings, passa para a funcao que verifica se ha numeros nessas strings e os adiciona em um dicionario
def createFirstDict(numbers):
        for i in range(0,len(numbers),2):
                #criara no dicionario chaves com o nome do arquivo e passara as strings de conteudo para uma funcao trata essas strings e extrai os numeros
                allNumbersFound.setdefault(numbers[i],findAllNumbers(numbers[i+1]))

#passa meu diretorio atual para a funcao que verifica e le os arquivos de texto
verifyDir(os.getcwd())

#chama a funcao criar dicionario para tratar os numeros da lista de numeros encontrados 
createFirstDict(infosFound)

#encontra numeros de telefone a partir de padroes especificos
def findCelNumbers(numbers,mode):
        #verificacao simples para numeros com ddd
        if mode == 1 or 'simple':
                var = re.compile(r'''
                479+\d{8}
                |0479+\d{8}
                |47+\d{8,9}
                |047+\d{8,9}
                ''', re.VERBOSE)
                v1 = var.findall(numbers)
        #verificacao media para numeros sem ddd
        if mode == 2 or 'medium':
                var = re.compile(r'''
                9*\d{8}
                |88*\d{6}
                ''', re.VERBOSE)
                v1 = var.findall(numbers)
        #verificacao completa de todas os parametros
        if mode == 0 or 'full':
                var = re.compile(r'''
                479+\d{8}
                |0479+\d{8}
                |47+\d{8,9}
                |047+\d{8,9}
                |9+\d{8}
                |88+\d{6}
                ''', re.VERBOSE)
                v1 = var.findall(numbers)
        if v1 != []:
                return v1

for num in allNumbersFound:
        for i in range(len(allNumbersFound[num])):
                t = findCelNumbers(allNumbersFound[num][i],0)
                if t == None:
                        continue
                else:
                        celNumbersFound.setdefault(num,t)

validNumber = []
def validateNumbers(numbers):
        if numbers == '88210000':
                pass
        else:
                validNumber.append(numbers)
pprint.pprint(celNumbersFound)




'''

Adicionar +55 aos numeros e salvar no banco de dados

'''

