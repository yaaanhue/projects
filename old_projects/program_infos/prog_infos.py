#coding=UTF-8
print('this a your program to save util informations \n')
print('informations:')

def f_cmd(text=''):
    import os
    os.system(text)

input_1 = input('1. Properties of foods \n2. cities and food prices \n3. Arithmetic calculation \n4. Infomations about Ant \n5. how does work eletric shower? \n\n') #input user to navegation in the main menu
if input_1 == 1:    #if selecioned option 1 in the main menu
    f_cmd('clear')
    input_2 = input('1. Tea mate (chá mate) \n2. Guava (goiabada) \n') #if selecioned option 1 in the main menu
    if input_2 == 1:    #if selecioned option 1 tea mate in the second menu
        f_cmd('clear')
        input_3 = input('1. Informations about tea mate \n2. Tabel properties tea mate \n3. Summary about tea mate \n\n')
        if input_3 == 1:    #if selecioned option 1 informations in the third menu -- menu inside second menu
            f_cmd('google-chrome https://www.trocandofraldas.com.br/cha-mate/')
        if input_3 == 2:    #if selecioned option 2 tabel properties in the third menu -- menu inside second menu
            f_cmd('display infos/tabel_properties_tea_mate.png')
        if input_3 == 3:    #if selecioned option 3 "summary about tea" in the third menu -- menu inside second menu
            f_cmd('gedit infos/summary_tea_mate')
            f_cmd('google-chrome https://www.trocandofraldas.com.br/cha-mate/')
    if input_2 == 2:     #if selecioned option 2 guava in the second menu
        f_cmd('clear')
        input_3 = input('1. Infomations about guava \n2. Tabel properties guave \n')
        if input_3 == 1:    #if selecioned option 1 informations in the third menu -- menu inside second menu
            f_cmd('google-chrome http://souagro.com.br/beneficios-da-goiaba-para-a-saude/')
        if input_3 == 2:    #if selecioned option 2 tabel properties in the third menu -- menu inside second menu
            f_cmd('google-chrome https://www.dietaesaude.com.br/dietas/alimentos/409-goiabada?q=goiabada')
if input_1 == 2:        #if selecioned option 2 in the main menu
    f_cmd('clear')
    input_2 = input('1. Alto paraiso \n2. Other \n')
    if input_2 == 1:    #if selecioned option Alto paraiso in the second menu
        f_cmd('clear')
        input_3 = input('1. Banana \n2. Oat (aveia) \n3. Apple (maçã) \n4. White Raisin (uva passa branca) \n')
        if input_3 == 1:    #if selecioned option 1 Banana in the third menu -- menu inside second menu
            f_cmd('clear')
            print ("Price of the banana: \n")
            price_banana = 3.38
            print ('R$/Kg',price_banana)
        if input_3 == 2:    #if selecioned option 2 Oat in the third menu -- menu inside second menu
            f_cmd('clear')
            print ("Price of the oat: \n")
            price_oat = 7.00
            print ('R$/Kg = ', price_oat)
        if input_3 == 3:    #if selecioned option 3 Apple in the third menu -- menu inside second menu
            f_cmd('clear')
            print ("Price of the apple: \n")
            price_apple = 8.78
            print ('R$/Kg = ', price_apple)
        if input_3 == 4:    #if selecioned option 4 White Raisin in the third menu -- menu inside second menu
            f_cmd('clear')
            print ("Price of the white raisin: \n")
            price_w_raisin = 25.00
            print ('R$/Kg = ', price_w_raisin)
    if input_2 == 2:
        f_cmd('clear')
if input_1 == 3:    #if selecioned option 3 in the main menu
    f_cmd('clear')
    input_2 = input('1. Addition \n2. Subtraction \n3. Division \n4. Multiplication ')
    if input_2 == 1:    #if selecioned option 1 adition in the second menu
        f_cmd('clear')
        print "let's make an addition account: \n"
        num_1 = input('type a first number: ')
        num_2 = input('type a second number: ')
        num_3 = input('type a third number: ')
        result_operation = num_1 + num_2 + num_3
        print '\nthe result of this operaction of addition is: ',result_operation
    if input_2 == 2:    #if selecioned option 2 subtraction in the second menu
        f_cmd('clear')
        print "let's make an subtraction account: \n"
        num_1 = input('type a first number: ')
        num_2 = input('how much do you want subtract from that number? ')
        result_operation = num_1 - num_2
        print '\nthe result of this operaction of subtraction is: ',result_operation
    if input_2 == 3:    #if selecioned option 3 division in the second menu
        f_cmd('clear')
        print "ok, let's divide some numbers."
        num_1 = input('enter a number ')
        num_2 = input('how much do you want divide this number? ')
        result_operation = num_1 / num_2
        print '\n the result of this multiplication is: ', result_operation
    if input_2 == 4:    #if selecioned option 4 multiplication in the second menu
        f_cmd('clear')
        print ("ok, let's multiply some numbers.")
        num_1 = input('enter the number to be multiplied ')
        num_2 = input('enter the number of times to be multiplied ')
        result_operation = num_2 * num_1
        print ('the result of this multiplication is: ', result_operation)
if input_1 == 4:    #if selecioned option 4 Ant in the main menu
    f_cmd('clear')
    input_2 = input('1. Some informations about ants \n2. Some other informations about ants \n')
    if input_2 == 1:    #if selecioned option 1 informations in the second menu
        f_cmd('google-chrome https://super.abril.com.br/ciencia/o-segredo-das-formigas/')
if input_1 == 5:    #if selecioned option 5 "eletric shower" in the main menu
    f_cmd('google-chrome https://www.mundodaeletrica.com.br/como-funciona-um-chuveiro-eletrico/')
input_1 = str(input_1)
file = open('name.txt', mode='w')
file.write(input_1)
file.close()
