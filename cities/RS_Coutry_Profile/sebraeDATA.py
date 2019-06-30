import requests, bs4, pprint, os, wget, time, socket
from wget import download

listCity = requests.get('https://datasebrae.com.br/perfil-dos-municipios-gauchos/')

htmlPage = bs4.BeautifulSoup(listCity.text,features='html.parser')

mainUrl = 'https://datasebrae.com.br'


os.chdir('pdf_files_downloaded')
city = 4
cities = htmlPage.find_all('a')
for city in range(len(htmlPage.find_all('a'))):
    if cities[city].get('href').startswith('/municipios/rs/Perfil'):
        filename = wget.download(mainUrl + str(cities[city].get('href')))
        print(city)
        time.sleep(10)
                
