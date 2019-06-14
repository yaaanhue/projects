#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http:/nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) 	#faz rolagens para o fim da pagina
#htmlElem.send_keys(Keys.HOME)	#faz rolagens para o inicio da pagina


'''
	O Selenium tem um modulo para teclas que sao impossiveis de digitar em um valor de string
	que funciona de modo muito semelhante aos caracteres de escape. Esses valores
	sao armazenados em atributos no modulo selenium.webdriver.common.keys
	Como esse eh um nome de modulo bem extenso, sera muito mais facil executar from selenium.webdriver.common.keys import Keys
	no inicio de seu programa; se fizer isso, voce podera simplesmente escrever Keys em qualquer lugar que devesse normalmente escrever selenium.webdriver.commom.Keys
'''