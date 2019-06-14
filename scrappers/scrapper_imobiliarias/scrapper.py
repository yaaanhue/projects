
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, pprint, time
from bs4 import BeautifulSoup as bs

#-------------- Chrome config
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

#chrome_driver = os.getcwd() + "/chromedriver_linux/chromedriver"    #driver selenium linux 
chrome_driver = os.getcwd() + "/chromedriver_win32/chromedriver"    #driver selenium windows
gdriver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)

#-------------

temp_url = 'https://www.google.com/search?q=imobiliarias+meia+praia&ei=hGXlXO6lI5bY5OUPyfWNIA&start=0&sa=N&ved=0ahUKEwju96iCta_iAhUWLLkGHcl6AwQ4ChDy0wMIcA&biw=1360&bih=685'

gdriver.get(temp_url)
googlePage = bs(gdriver.page_source, 'html.parser')
#-------------------------------------------------------------
#encontra link da proxima pagina de resultado do google
#o link esta dentro de uma tabe;a
tr_NextUrl = googlePage.find('tr', {'valign': 'top'})
#encontra todos os objetos link <a> dentro dessa tabela
td_withNexturl = tr_NextUrl.find_all('a')

linksNextPage = []
#percorre cada objeto <a> para pegar os links href e salva na lista LinksNextPage
for link_next in range(len(td_withNexturl)):
    linksNextPage.append(td_withNexturl[link_next].get('href'))

htmlPages_retuls = []
#pega todos os links da lista menos o ultimo link pois eh repeticao do link da primeira page (erro do google?)
for i in range((len(linksNextPage)-1)):
    #cria uma lista com todos os codigos fonte dos links encontrados 
    gdriver.get(temp_url + linksNextPage[i])
    htmlPages_retuls.append(bs(gdriver.page_source, 'html.parser'))
#--------------------------------------------------------------

links = []  #links das imobiliarias
def findLinksImobiliarias(htmlPage):
    #encontra a div com os links das imobiliarias e os salva na lista links 
    divSrg = htmlPage.find_all('div',{'class':'srg'})
    divs_R = divSrg[0].find_all('div', {'class':'r'})
    for link in range(len(divs_R)):
        links.append(divs_R[link].find('a').get('href'))

for i in range(len(htmlPages_retuls)):
    findLinksImobiliarias(htmlPages_retuls[i])

fileLinks = open('linksImobiliarias.txt','a')
for i in range(len(links)):
    print(str(i) + '-'  + links[i])
    fileLinks.write(str(links[i]) + '\n')
fileLinks.close()


'''
Adicionar os dados ao banco de dados

Encontrar telefones e emails nos sites extraidos

Adicionar mais cidades no banco de dados
'''