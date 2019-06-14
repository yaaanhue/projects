
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

url = 'https://www.google.com/search?q=imobiliarias+meia+praia&ei=hGXlXO6lI5bY5OUPyfWNIA&start=0&sa=N&ved=0ahUKEwju96iCta_iAhUWLLkGHcl6AwQ4ChDy0wMIcA&biw=1360&bih=685'

gdriver.get(url)
googlePage = bs(gdriver.page_source, 'html.parser')
divSrg = googlePage.find_all('div',{'class':'srg'})
divs_R = divSrg[0].find_all('div', {'class':'r'})

links = []
for link in range(len(divs_R)):
    links.append(divs_R[link].find('a').get('href'))

#encontra link da proxima pagina de resultado do google
#o link esta dentro de uma tabe;a
tr_NextUrl = googlePage.find('tr', {'valign': 'top'})
#encontra todos os objetos link <a> dentro dessa tabela
td_withNexturl = tr_NextUrl.find_all('a')

linksNextPage = []
#percorre cada objeto <a> para pegar os links href e salva na lista LinksNextPage
for link_next in range(len(td_withNexturl)):
    linksNextPage.append(td_withNexturl[link_next].get('href'))

for i in range((len(linksNextPage)-1)):
    linksNextPage[i] = url + linksNextPage[i]

pprint.pprint(linksNextPage)
#time.sleep(2)
#url com a proxima pagina do google
#url = urlNextPage + url
#pprint.pprint(links)
