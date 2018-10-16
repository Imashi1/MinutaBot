def getData():
    # Creacion de diccionario con la data necesaria por dias y respectivos tipos de almuerzo
    dicc = dict()
    for i in range(0,6):
        dicc[i] = [[], [], [], [], [], [],[]]#->solucion 9/10/2018
    arch = open("Almuerzos.txt")
    row = 0
    column = -1
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

                #print (linea)
                #print (row, column)
                #print(dicc[row][column])
                #print(dicc[1][6]) ->> problema 9/20/2018
                dicc[row][column].append(linea)
    arch.close()
    return dicc

def getCurrentDayAndIndex(dicc, day):
    index = 0
    dia = 'nah'
    for value in dicc[0]:
        if value != []:
            _, numero = value[0].split()
            if int(day) == int(numero):
                index = dicc[0].index(value)
                dia = value[0]
                break
    return dia, index
'''
{'0' = [Lu, Ma, Mi, Jue, Vi]}

'''
