def getArchives():
	dicc = dict()
	for i in range(0,6):
		dicc[i] = list()
	arch = open("Almuerzos.txt")
	for linea in arch:
		if "-" not in linea:
			linea = linea.strip()
