#!/usr/bin/python

'''
	Se voce abrir as ferramentas de desenvolvedor do navegador e inspecionar
	os elementos da pagina, encontrara o seguinte:

	* o URL do arquivo de imagem dado pelo atributo href de um elemento <img>.

	* o elemento <img> esta em um elemento <div id="(campo id)">.

	* o botao Prev/Next (anterior ou proxima imagem) tem um atributo HTML rel cujo valor eh "Prev"
'''


import requests, os, bs4
'''
	Voce tera uma url que comeca com http://xkdc.com ela sera repetidamente atualizada
	(em um loop for) com o URL do link proxima ou anterior. A cada passo no loop, a imagem em url sera baixada.
	Voce sabera que o loop deve ser encerrado quando url terminar com "#"
'''

url = 'http://xkdc.com'	#url inicial do site com as imagens
os.makedirs('xkdc')		#cria o diretorio pra salvar as imanges
while not url.endswith('#'):
	#TODO: Faz donwload da pagina.
	print('Downloading page %s...' % url)
	res = request.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	'''
		Exibe a URL para que o usuario saiba qual url o programa esta prestes a baixar;
		entao utilize a funcao request.get() do modulo requests para fazer o download.
		Como Sempre, voce chamara o metodo raise_for_status() do objeto response imediatamante
		para lancar uma excecao e encerrar o programa caso um erro tenha ocorrido no download.
	'''

	#TODO: Encontra o URL da imagem.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')


	#TODO: Faz o download da imagem.
	print('Downloading image %s...' % (comicUrl))
	res = requests.get(comicUrl)
	res.raise_for_status()

	'''
	A partir da inspecao da pagina inicial de XKDC.COM de com suas ferramentas de desenvolvedor, sabemos que o elemento <img>
	para a imagem da tirinha esta em um elemento <div> com o atributo id definido com comic, portanto o seletor '#comid img'
	fara voce obter o elemento <img> correto do objeto BeautifulSoup.

	'''

	#TODO: Salva a imagem em "imagens baixadas"
	imageFile = open(os.path.join('xkdc', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#TODO: obtem o url do botao para a proxima imagem ou anterior
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkdc.com' + prevLink.get('href')

	print('Done.')


'''
	o arquivo de imagem da tirinha esta armazenado na variavel res. Sera necessario ter um nome para o arquivo que contera a imagem local;
	esse nome devera ser passado para open(). comicUrl tera um valor como http://imgs.xkdc.com/comics/heartbleed_explanation,png
	que conforme voce deve ter percebido parece muito com um path de arquivo. Com efeito, podemos chamar os.path.basename() com comicUrl
	e ele retornara somente a ultima parte do URL, ou seja, heartbleed_explanation.png.
	Podemos usar isso como nome do arquivo quando salvarmos a imagem no disco rigido. Junte esse nome ao nome da sua pasta xkdc usando os.path.join()
	para que seu programa utilize barras invertidas (\) no Windows e barras para frente (/) no linux ou OS X. 

	Agora finalmente temos um nome para o arquivo, podemos chamar open() para abrir um novo arquivo em modo 'wb' de escrita binaria.
	Conforme vimos anteriormente, para salvar arquivos baixados com requests, devemos percorrer o valor de retorno do metodo iter_content() com um loop.
	O codigo do loop for grava porcoes de dados da imagem (no maximo 100.000 bytes de cada vez) no arquivo e, em seguida, o arquivo sera fechado. A imagem agora esta salva

	Depois disso, o seletor 'a[rel="prev"]' identifica o elemento <a> cujo atributo rel esta definido com prev(proximo/anterior) e o atributo href desse elemento <a> podera 
	ser usado para obter o URL da tirinha anterior, que sera armazenado em url. Entao o loop while comecara todo o processo de download novamente para essa tirinha


'''