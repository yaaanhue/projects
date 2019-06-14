from sklearn import tree

lisa = 1
irregular = 0
maca = 1
laranja = 0

pomar =[[150, lisa], [130, lisa], [180, irregular], [160, irregular]]

resultado = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Entre com o peso: ")
superficie = input("Entre com a superficie: (1 para lisa e 0 para irregular)")

resultadousuario = clf.predict([[peso, superficie]])

if resultadousuario == 1:
	print("eh uma maca")
else:
	print("eh uma laranja")
