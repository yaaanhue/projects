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

urlProfile = 'https://www.instagram.com/marcelotraderfx/'
driver.get(urlProfile)

htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')

profilesInfo = {}

nameAndUser = htmlPage.find('div',{'class':'v9tJq'}).find_all('h1')
profilesInfo.setdefault('user',nameAndUser[0].text)
profilesInfo.setdefault('name',nameAndUser[1].text)

profilesInfoFound = htmlPage.find('header').find_all('span')

profilesInfo.setdefault('posts',profilesInfoFound[1].text)
profilesInfo.setdefault('followers',profilesInfoFound[2].text)
profilesInfo.setdefault('following',profilesInfoFound[3].text)
profilesInfo.setdefault('bio',{})
profilesInfo['bio'].setdefault('text',profilesInfoFound[4].text)
profilesInfo['bio'].setdefault('strings',profilesInfoFound[4].text.split())
for s in profilesInfoFound[4].find_all('a'):
    if s.get('href').startswith('/explore/tags'):
        profilesInfo['bio'].setdefault('tags',[])
        profilesInfo['bio']['tags'].append(s.get('href'))
    else:
        profilesInfo['bio'].setdefault('profiles',[])
        profilesInfo['bio']['profiles'].append(s.get('href'))

linksFound = []

while len(linksFound) < int(profilesInfo['posts']):
    links_in_Profile = htmlPage.find_all('a')
    for l in range(len(links_in_Profile)):
        if links_in_Profile[l].get('href').startswith('/p/'):
            linksFound.append('https://www.instagram.com' + str(links_in_Profile[l].get('href')))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(3)
    htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
    linksFound = list(set(linksFound))
    print('links limpos: ' + str(len(linksFound)))
print(('links encontrados: ' + str(len(linksFound))))

'''

Falta somente pegar as informacoes de cada postagem

'''