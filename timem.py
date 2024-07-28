from datetime import datetime

# Función para calcular la diferencia entre dos horas
def calcular_diferencia(hora1: datetime, hora2:datetime):
    formato = "%H:%M"
    h1 = datetime.strptime(hora1, formato)
    h2 = datetime.strptime(hora2, formato)
    diferencia = h2 - h1
    return diferencia

# Leer el archivo y procesar las líneas
resultados = {}
with open('t1.txt', 'r') as archivo:
    for linea in archivo:
        partes = linea.strip().split()
        hora1 = partes[0]
        hora2 = partes[1]
        nombre = partes[2]
        diferencia = calcular_diferencia(hora1, hora2)
        if nombre in resultados:
            resultados[nombre] += diferencia
        else:
            resultados[nombre] = diferencia

# Mostrar los resultados
for nombre, diferencia in resultados.items():
    print(f"{nombre}: {diferencia}")

# Guardar los resultados en una lista
lista_resultados = [(nombre, diferencia) for nombre, diferencia in resultados.items()]