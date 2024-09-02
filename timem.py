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
resultado = datetime.strptime("00:00", "%H:%M")
with open(sys.argv[1], 'r') as archivo:
    for linea in archivo:
        partes = linea.strip().split()
        horas = []
        for i in partes:
            if i[0].isdigit() == True:
                horas.append(i)
            else:
                nombre = i

        diferencia = calcular_diferencia(horas[0], horas[1])
        resultado += diferencia
        if nombre in resultados:
            resultados[nombre] += diferencia
        else:
            resultados[nombre] = diferencia

# Mostrar los resultados
for nombre, diferencia in resultados.items():
    print(f"{nombre}: {diferencia}")
print("Total de horas: " + str(resultado))

# Guardar los resultados en una lista
lista_resultados = [(nombre, diferencia) for nombre, diferencia in resultados.items()]