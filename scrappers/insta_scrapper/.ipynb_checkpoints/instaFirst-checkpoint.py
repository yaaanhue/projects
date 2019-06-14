#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os, pprint, time, bs4, re, re

#directory to find chrome webdriver
chrome_driver = os.getcwd() + "/chromedriver"

#instance a chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size-1920x1080')


#go to link
driver =  webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
nameLocation = input()
linkLocation = input()
driver.get(linkLocation)

# execute script to scroll down the page and sleep for 3s
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)

    
sourceContent = driver.page_source
bSoup = bs4.BeautifulSoup(sourceContent, features="html.parser")
content = bSoup.select('span a')

endLink = []
for link in bSoup.findAll('a', attrs={'href': re.compile(r'^/p')}):
    endLink.append(link.get('href'))


os.makedirs(nameLocation)
url = []
os.chdir('/home/yan/prog/python/projects/selenium/instaFirst/' + nameLocation)
for i in range(len(endLink)):
    url.append('https://instagram.com' + endLink[i])
    driver.get(url[i])
    name = str(i) + '.txt'
    saveFile = open(name,'w')
    saveFile.writelines(driver.page_source)
    saveFile.close()
print(str(len(url)) + ' URLs found')

'''
    Os links para as publicacoes estao dentro de <span id='react-root'><a href='link imagem'>

    a partir do link da imagem da para ver quem a publicou, quando, numero de curtidas e os usuarios que comentaram 
        - pegar usuarios e fazer o scrapper em seus perfis
        - em suas publicacoes, pegar usuarios que comentaram, localizacoes e o programa segue pra frente fazendo o mesmo com o que encontrar
'''

'''
    o programa faz scroll a cadaa tres segundos para que carregue as imagens e se possa pegar o html atualizado com os links das novas publicacoes carregadas
'''