from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import bs4, time, pprint

#directory to find chrome webdriver
chrome_driver = r'C:\Users\Yan\Desktop\git\projects\scrappers\insta_scrapper\chromedriver_win32\chromedriver.exe'

#instance a chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size-1920x1080')

driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

linkPub = 'https://www.instagram.com/p/By2hKC9gNVr/'


driver.get(linkPub)

htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')
publication = {}
profileName = htmlPage.find('h2',{'class':'BrX75'}).find('a').get('href')
publication.setdefault(profileName,{})
publication[profileName].setdefault('subtitle',{})
for linkInLegend in htmlPage.find('ul',{'class':'XQXOT'}).find('li').find_all('a'):
    publication[profileName]['subtitle'].setdefault('text',htmlPage.find('ul',{'class':'XQXOT'}).find('li').text)
    if linkInLegend.get('href') != profileName and linkInLegend.get('href').startswith('/explore/tags/'):
        publication[profileName]['subtitle'].setdefault('tags',[])
        publication[profileName]['subtitle']['tags'].append(linkInLegend.get('href'))
    elif linkInLegend.get('href') != profileName and not (linkInLegend.get('href').startswith('/explore/tags/')):
        publication[profileName]['subtitle'].setdefault('profile',[])
        publication[profileName]['subtitle']['profile'].append(linkInLegend.get('href'))
        
publication[profileName].setdefault('comments',{})
publication[profileName].setdefault('likes',htmlPage.find('a',{'class':'zV_Nj'}).text)
publication[profileName].setdefault('date',htmlPage.find('time').get('datetime'))
if htmlPage.find('div',{'class':'JF9hh'}).find('a') != None:
    publication[profileName].setdefault('location',htmlPage.find('div',{'class':'JF9hh'}).find('a').get('href'))

for listComment in htmlPage.find_all('ul',{'class':'Mr508'}):
    publication[profileName]['comments'].setdefault(str(listComment.find('a').get('href')),{})
    if len(listComment.find_all('a')) < 3 and listComment.find_all('a')[0].get('href') == listComment.find_all('a')[1].get('href'):
        publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('text',listComment.find('span').text)
        publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('date-comment',listComment.find('time').get('datetime'))
    else:
        for link in listComment.find_all('a'):
            publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('date-comment',listComment.find('time').get('datetime'))
            publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('text',listComment.find('span').text)
            if link.get('href').startswith('/explore/tags/'):
                publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('tags',[])
                publication[profileName]['comments'][str(listComment.find('a').get('href'))]['tags'].append(link.get('href'))
            elif link.get('href') != str(listComment.find('a').get('href')):
                publication[profileName]['comments'][str(listComment.find('a').get('href'))].setdefault('profiles',[])
                publication[profileName]['comments'][str(listComment.find('a').get('href'))]['profiles'].append(link.get('href'))

pprint.pprint(publication)

