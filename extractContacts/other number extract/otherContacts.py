import os, re, pprint  

celNumbers = {}
fixNumbers = {}

def findAllNumbers(listStrings):
    #cria uma lista temporaria para armazenar os numeros que encontra
    numbers = []
    #fara uma interacao por cada string da lista de strings passando por toda ela
    for size in range(len(listStrings)):
        #verifica se ha numeros na string, se houver ira salvar na variavel auxiliar tempNum
        tempNum = ''.join(filter(str.isdigit, listStrings[size]))
        #ira salvar na lista apenas o grupo de numeros com pelo menos 8 caracteres
        if len(tempNum) > 8:
            numbers.append(tempNum)
        else:
            continue
        #retorna a lista de numeros encontrados para depois ser armazenado no dicionario
    return numbers    

def findNumbers(numbers):
#funcao que encontra numeros de telefone em strings
    var = re.compile(r'''
    479+\d{8}
    |0479+\d{8}
    |47+\d{8,9}
    |047+\d{8,9}
    |9+\d{8}
    |88+\d{6}
    |3+\d{7}    
    ''', re.VERBOSE)
    v1 = var.findall(str(numbers))
    if v1 != []:
        return v1

def completeNumbers(nameKey,celNumbers):
    #funcao que completa os numeros de celular com +55 no inicio
    temp = []
    if celNumbers != None:
        for i in range(len(celNumbers)):
            temp.append('+55' + str(celNumbers[i]))
        contacts.setdefault(str(nameKey),temp)

numbers = {} #salva os numeros sem tratamento algum
contacts = {} #salva os numeros de contatos encontrados ja atualizados com +55

os.chdir(r'C:\Users\Yan\Desktop\git\extractContacts\scannedFiles')
for txtFile in os.listdir('.'):
    if txtFile.endswith('.txt'):
        fileObj = open(txtFile,'r',encoding='UTF-8')
        numbers.setdefault(str(txtFile),findNumbers(findAllNumbers(fileObj.readlines())))   #salva os numeros sem tratamento
        completeNumbers(str(txtFile),numbers[str(txtFile)])

for keyName in contacts.keys():
    fixNumbers.setdefault(str(keyName),[])
    celNumbers.setdefault(str(keyName),[])
    for string in range(len(contacts[keyName])):
        if contacts[keyName][string].startswith('+553' or '+55473' or '+550473'):
            fixNumbers[str(keyName)].append(contacts[keyName][string])
        else:
            celNumbers[str(keyName)].append(contacts[keyName][string])
    
    if fixNumbers[str(keyName)] == []:
        del fixNumbers[str(keyName)]
pprint.pprint(len(fixNumbers))
pprint.pprint(celNumbers)
    