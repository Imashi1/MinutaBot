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

def getCurrentDayAndIndex(dicc, day):
	index = 0
	dia = 'nah'
	for value in dicc[0]:
		if value != []:
			_, numero = value[0].split()
			if str(day) == numero:
				index = dicc[0].index(value)
				dia = value[0]
				break
	return dia, index
'''
{'0' = [Lu, Ma, Mi, Jue, Vi]}

'''