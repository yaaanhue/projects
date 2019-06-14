#!/usr/bin/python3
#Programa para pegar informacoes de perfis do instagram
#program to get instagram profile information

'''
	Writed by Yan Hue - Escrito por Yan Hue
	https://github.com/yaaanhue
'''

import requests, os, bs4

#pergunta qual pagina quer baixar o codigo
#question what page do you want to download the code
wantDownloadThisPage = input('What page do you want download source code? \nInsert text that comes after the "@" >> ')

#baixa o codigo da pagina 
#download page source code
pageInstaText = requests.get('https://www.instagram.com/' + wantDownloadThisPage)

#verificar se o link existe e pode ser baixado
#verify if link exists and can be downloaded
try:
	pageInstaText.raise_for_status()
except Exception as exc:
	print('Erro: %s' % (exc))

#verifica se baixou tudo certo e lista o numero de caracteres no texto
#verify download be ok and ist the number of characters in the text
if pageInstaText.status_code == requests.codes.ok:
	print('\nDownloaded page with ' + str(len(pageInstaText.text)) + ' characters in the text')

#salvar o codigo em um arquivo de texto chamado com o nome de usuario
#save the code in a text file named with the username 
playFile = open(wantDownloadThisPage + '.txt', 'wb')
for pieceOfText in pageInstaText.iter_content(100000):
	playFile.write(pieceOfText)
playFile.close()
print('Saved file named ' + wantDownloadThisPage + '.txt')


