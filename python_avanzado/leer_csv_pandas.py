import pandas as pd
# Leer el archivo csv
#archivo = pd.read_csv("archivo_datos.csv")
# Imprimir el archivo
#print(archivo)

#usando la funcion read_csv para leer el archivo
df = pd.read_csv("archivo_datos.csv",names=["name","lastname","age"])
#cambio los nombres de las columnas
nombres = df["name"]
#print(df)

#ordenando el dataframe por la columna edad
df_ordenado = df.sort_values(by="age")

#concatenando los dataframes
df_concatenado = pd.concat([df,df_ordenado])

#imprimiendo las primeras 2 filas
primeras_filas = df.head(2)

#accediendo a las ultimas 3 filas con tail
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
cantidad_filas_columnas = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

print("********DF ORDENADO******************************\n")
print(df_ordenado)
print("********DF CONCATENADO******************************\n")
print(df_concatenado)
print("********PRIMERAS FILAS******************************\n")
print(primeras_filas)
print("********ULTIMAS FILAS******************************\n")
print(ultimas_filas)
print("*********CANTIDAD DE FILAS Y COLUMNAS*****************************\n")
print(cantidad_filas_columnas)
print("*********INFORMACION DF *****************************\n")
print(df_info)
