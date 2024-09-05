from datetime import datetime
import sys

# Función para calcular la diferencia entre dos horas
def calcular_diferencia(hora1: datetime, hora2:datetime):
    formato = "%H:%M"
    h1 = datetime.strptime(hora1, formato)
    h2 = datetime.strptime(hora2, formato)
    diferencia = h2 - h1
    return diferencia

# Leer el archivo y procesar las líneas
resultados = {}
descripciones = {}
hora_previa = ""
resultado = datetime.strptime("00:00", "%H:%M")
with open(sys.argv[1], 'r') as archivo:

    for linea in archivo:
        descripcion_aux = ""
        partes = linea.strip().split()
        horas = []
        en_parentesis = 0
        for i in partes:
            if en_parentesis == 1:
                if i[-1] == ')':
                    en_parentesis = 0
                    descripcion_aux += " " + i[:-1]
                else:
                    descripcion_aux += " " + i
            elif i[0].isdigit() == True:
                horas.append(i)
            elif i[0] == '(':
                if i[-1] == ')':
                    descripcion_aux = i[1:-1]
                else:
                    descripcion_aux = i[1:]
                    en_parentesis = 1
            else:
                nombre = i
        
        if len(horas) == 1:
            horas.insert(0, hora_previa)

        hora_previa = horas[1]

        diferencia = calcular_diferencia(horas[0], horas[1])
        resultado += diferencia
        if nombre in resultados:
            resultados[nombre] += diferencia
        else:
            resultados[nombre] = diferencia

        if (descripcion_aux == ""):
            descripcion_aux = "non-specified"

        if nombre not in descripciones:
            descripciones[nombre] = {}

        if descripcion_aux in descripciones[nombre]:
            descripciones[nombre][descripcion_aux] += diferencia
        else:
            descripciones[nombre][descripcion_aux] = diferencia


# Mostrar los resultados
for nombre, diferencia in resultados.items():
    print(f"{nombre}: {diferencia}")
    if nombre in descripciones:
        for i in descripciones[nombre]:
                print(f"   + {i}: {descripciones[nombre][i]}")
print("Total de horas: " + str(resultado.hour) + ":" + str(resultado.minute))

# Guardar los resultados en una lista
lista_resultados = [(nombre, diferencia) for nombre, diferencia in resultados.items()]