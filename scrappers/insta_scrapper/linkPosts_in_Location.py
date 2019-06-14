from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import bs4, time, pprint

#directory to find chrome webdriver
chrome_driver = r'C:\Users\Yan\Desktop\git\scrappers\insta_scrapper\chromedriver_win32\chromedriver'

#instance a chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size-1920x1080')

driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

url = input('Insira a url da localizacao que deseja pegar os links  ')
#url = 'https://www.instagram.com/explore/locations/234636166/uniao-da-vitoria/'

driver.get(url)
htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')

places = {}
places.setdefault('uniao-da-vitoria',{})

places['uniao-da-vitoria'].setdefault('url-Location', url)
places['uniao-da-vitoria'].setdefault('latitude',htmlPage.find('meta',{'property':'place:location:latitude'}).get('content'))
places['uniao-da-vitoria'].setdefault('longitude',htmlPage.find('meta',{'property':'place:location:longitude'}).get('content'))

linksFound = []

links1 = htmlPage.find_all('a')
for l in range(len(links1)):
    if links1[l].get('href').startswith('/p/'):
        linksFound.append('https://www.instagram.com' + str(links1[l].get('href')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
links1 = htmlPage.find_all('a')
for l in range(len(links1)):
    if links1[l].get('href').startswith('/p/'):
        linksFound.append('https://www.instagram.com' + str(links1[l].get('href')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
links1 = htmlPage.find_all('a')
for l in range(len(links1)):
    if links1[l].get('href').startswith('/p/'):
        linksFound.append('https://www.instagram.com' + str(links1[l].get('href')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
links1 = htmlPage.find_all('a')
for l in range(len(links1)):
    if links1[l].get('href').startswith('/p/'):
        linksFound.append('https://www.instagram.com' + str(links1[l].get('href')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(3)
htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
links1 = htmlPage.find_all('a')
for l in range(len(links1)):
    if links1[l].get('href').startswith('/p/'):
        linksFound.append('https://www.instagram.com' + str(links1[l].get('href')))


print(len(linksFound))
linkProfiles = list(set(linksFound))
print(len(linkProfiles))
pprint.pprint(linkProfiles)



'''

pegar o nome da localizacao e adicionar no dicionario
Ha o numero de publicacoes no source code
Falta incluir o scroll em uma funcao para que rode ate o fim da pagina e pegue todos os links da localizacao.

'''