from bs4 import BeautifulSoup
import requests
import os, os.path, csv
import re
import pandas as pd

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

Almuerzo=[]

listingurl="https://www.usm.cl/comunidad/servicio-de-alimentacion/"

response = requests.get(listingurl)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table")[0]
new_table = pd.DataFrame(columns=range(0,6), index = [0])

row_marker = 0
for row in table.find_all('tr'):
	column_marker = 0
	print (row)
	columns = row.find_all('td')
	for column in columns:
		print(column)
		new_table.iat[row_marker,column_marker] = column.get_text()
		column_marker += 1
	print("------------------")


'''
Data = open('Data.txt','w')
for rows in soup.find_all("table"):
    limpio = cleanhtml(rows)
    print(rows)
    Data.write(limpio+'\n')
Data.close()
'''

'''
def obtenerAlmuerzos():
	arch = open("Data.txt")
	almuerzos = False
	dietas = False
	cenas = False
	vegetariano = False
	dia = 1
	# Creacion de listas para los alimentos
	listaAlmuerzos = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': []}
	listaDietas = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': []}
	listaVegetariano = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': []}
	listaCenas = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': []}

	# Creacion de diccionario para los dias
	dicc = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': []}
	for linea in arch:
		linea = linea.strip()
		# Condicionales para agregar el dia correspondiente.
		if "Lunes" in linea:
			dia, numero = linea.split()
			dicc["Lunes"].append(dia)

		elif "Martes" in linea:
			dia, numero = linea.split()
			dicc["Martes"].append(dia)

		elif "Miercoles" in linea:
			dia, numero = linea.split()
			dicc["Miercoles"].append(dia)

		elif "Jueves" in linea:
			dia, numero = linea.split()
			dicc["Jueves"].append(dia)

		elif "Viernes" in linea:
			dia, numero = linea.split()
			dicc["Viernes"].append(dia)

		else:
			if "Almuerzos" in linea:
				almuerzos = True
			elif "Dietas" in linea:
				almuerzos = False
				dietas = True
			elif "Vegetariano" in linea:
				dietas = False
				vegetariano = True
			elif "Cenas" in linea:
				vegetariano = False
				cenas = True
			else:
				if almuerzos:
					if "HASTA AGOTAR STOCK" in linea:
						dia = 2
					else:

	return
'''