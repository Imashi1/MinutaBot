def getData():
	# Creacion de diccionario con la data necesaria por dias y respectivos tipos de almuerzo
	dicc = dict()
	for i in range(0,5):
		dicc[i] = [[], [], [], [], [], []]
	arch = open("Almuerzos.txt")
	row = -1
	column = 0
	for linea in arch:
		if "!" in linea:
			row += 1
			column = 0
		elif "-" in linea:
			column += 1
		else:
			newRow = False
			linea = linea.strip()
			if linea != '':
				dicc[row][column].append(linea)
	arch.close()
	return dicc
'''
{'0' = [Lu, Ma, Mi, Jue, Vi]}

'''