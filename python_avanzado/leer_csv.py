#las siglas csv significan comma separated values, es decir, valores separados por comas.
#importamos la libreria de csv
import csv
with open("archivo_datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
