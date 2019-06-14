#!/usr/bin/python3
import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)	#configura a conexao com o servidor de email e porta
smtpObj.ehlo()	#confirma conexao com o servidor de email	-se retornar 250 significa que conectou-
smtpObj.starttls()	#inicia protocolo criptografia tls (porta 587)	-se retornar 220 servidor esta pronto-
passwd = input()
smtpObj.login('yaaanhue@gmail.com',passwd)	#faz login no servidor de email -se retornar 235 conectou-
#smtpObj.login('yaaanhue@gmail.com','gxnxlykbbkblsxoq')

inp = input()
text = 'Subject: So long.\n'+inp

smtpObj.sendmail('yaaanhue@gmail.com','machadonycolas3@gmail.com',text)	#envia email, pode colocar inumeros destinatarios -tem que comecar com Subject: \n

s = smtpObj.quit()
if s[0] == 221:
	print('Done')