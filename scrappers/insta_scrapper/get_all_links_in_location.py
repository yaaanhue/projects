from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import bs4, time, pprint

#directory to find chrome webdriver
chrome_driver = r'C:\Users\Yan\Desktop\git\projects\scrappers\insta_scrapper\chromedriver_win32\chromedriver'

#instance a chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size-1920x1080')

driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

#url = 'https://www.instagram.com/explore/locations/14633616/the-hall-club/'
url = input('insira a url da localizacao \n:')
driver.get(url)

htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
htmlElem = driver.find_element_by_tag_name('html')

title = htmlPage.find('meta',{'property':'og:description'}).get('content')
nameLocation = title[title.find('‘')+1:-1]

places = {}

places.setdefault(str(nameLocation),{})
places[str(nameLocation)].setdefault('latitude',htmlPage.find('meta',{'property':'place:location:latitude'}).get('content'))
places[str(nameLocation)].setdefault('longitude',htmlPage.find('meta',{'property':'place:location:longitude'}).get('content'))
places[str(nameLocation)].setdefault('url-Location', url)

linksFound = []
linkProfiles = []
debug = {}

numPublications = int(''.join(filter(str.isdigit, htmlPage.find('meta',{'name':'description'}).get('content')[:htmlPage.find('meta',{'name':'description'}).get('content').find('-')])))
print('{} publicacoes em {}'.format(numPublications,nameLocation))

temp = 0
stop = 0
while len(linkProfiles) < numPublications and stop != 3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(2)
    htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
    for links in htmlPage.find_all('a'):
        if links.get('href').startswith('/p/'):
            linksFound.append('https://www.instagram.com' + str(links.get('href')))
    linkProfiles = list(set(linksFound))
    if len(linkProfiles) == temp:
        htmlElem.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        htmlElem.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        htmlElem.send_keys(Keys.HOME)
        time.sleep(2)
        htmlElem.send_keys(Keys.END)
        htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
        if htmlPage.find('div',{'class':'Z2m7o'}).find('button') != None:
            debug.setdefault(str(len(linkProfiles)), [])
            debug[str(len(linkProfiles))].append(htmlPage.find('div',{'class':'Z2m7o'}).find('button').text)
            stop = 0
        elif str(len(linkProfiles)) not in debug.keys():
            stop += 1
            print('{} tentativa'.format(str(stop)))
        for links in htmlPage.find_all('a'):
            if links.get('href').startswith('/p/'):
                linksFound.append('https://www.instagram.com' + str(links.get('href')))
        linkProfiles = list(set(linksFound))
    temp = len(linkProfiles)
    print('{} links encontrados'.format(len(linkProfiles)))
places[str(nameLocation)].setdefault('LinksPublications', linkProfiles)
print('\nFINISH\nforam encontrados {} links das {} publicacoes na localizacao {} e programa encerrado.\n'.format(len(linkProfiles), numPublications, nameLocation))
pprint.pprint(places)




''' #funcao extra escreve os links em um documento de texto
    file = open('linksPublicacoes.txt', 'a')
    for l in linkProfiles:
        file.writelines(str(l) + '\n')
    file.close
'''
''' #outra possibilidade para pegar o nome da localizacao mas com ifens entre as palavras
    firstBar = url[44:].find('/')
    nameLocation = url[44+1+first:-1]
    print(nameLocation)
'''
