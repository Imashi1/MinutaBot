from bs4 import BeautifulSoup
import requests
import os, os.path, csv
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

Almuerzo=[]

listingurl="https://www.usm.cl/comunidad/servicio-de-alimentacion/"

response = requests.get(listingurl)

soup = BeautifulSoup(response.text, "html.parser")
Data = open('Data.txt','w')
for rows in soup.find_all("tr"):
    limpio = cleanhtml(rows)
    Limpio2= limpio[1:9999]
    Data.write(Limpio2+'\n')
Data.close()

Data= open('data.txt','r')
for leer in Data:
    cortar= leer.strip().split('\n')
    if 'Almuerzos' in cortar:
             
        
    print(cortar)
    
        

    
