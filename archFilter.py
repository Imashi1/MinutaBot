def getArchives():
	dicc = dict()
	for i in range(0,6):
		dicc[i] = [[], [], [], [], [], []]
	arch = open("Almuerzos.txt")
	row = 0
	for linea in arch:
		if "!" in linea:
			newRow = True
		elif newRow:
			linea = linea.strip()
			dicc[row].append(linea)
		elif "-" in linea:
			column += 1
