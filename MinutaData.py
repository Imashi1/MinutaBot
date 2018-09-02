from bs4 import BeautifulSoup
import requests
import os, os.path, csv
import re
from archFilter import *
from datetime import datetime


'''
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext
'''

def actualizarArchivos():
	status = open("status.txt")
	day = status.readlines()[0]
	status.close()

	#Obtencion del dia actual
	date = str(datetime.now())
	fecha,_ = date.split()
	anio, mes, dia = map(int,fecha.split('-'))

	#if int(day) != dia:
	if int(day) != dia:
		#Url de donde se consiguio la data 
		listingurl="https://www.usm.cl/comunidad/servicio-de-alimentacion/"

		#Procesamiento del archivo html
		response = requests.get(listingurl)
		soup = BeautifulSoup(response.text, "html.parser")
		table = soup.find_all("table")[0]
		row_marker = 0

		#Creacion de archivo donde cada ! es una fila y cada - es una columna
		Data = open('Almuerzos.txt', 'w')
		for row in table.find_all('tr'):
			column_marker = 0
			columns = row.find_all('td')
			Data.write("!\n")
			for column in columns:
				Data.write(column.get_text() + "\n")
				column_marker += 1
				Data.write("-\n")
			row_marker += 1

		Data.close()

		#Obtencion del diccionario de almuerzos
		diccionario = getData()
		day, index = getCurrentDayAndIndex(diccionario, dia)
		infoDelDia = open('info.txt', 'w')
		status = open('status.txt', 'w')
		if day == 'nah':
			status.write(str(dia))
			infoDelDia.write('No hay informacion disponible para hoy.\n')
		else:
			infoDelDia.write(day+"\n\n")
			status.write(str(dia))
			del diccionario[0]
			for _,values in diccionario.items():
				infoDelDia.write(values[0][0] + "\n")
				for dato in values[index]:
					infoDelDia.write(dato + "\n")
				infoDelDia.write("\n")

		infoDelDia.close()
		status.close()

actualizarArchivos()
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