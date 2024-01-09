#abro el archivo txt.
#archivo = open("texto_prueba.txt", encoding="utf-8")
#leo el archivo completo
# linea = archivo.read()

#Otra forma de abrir el archivo mas segura
with open("texto_prueba.txt", encoding="utf-8") as archivo:
    #leo el archivo completo
    linea = archivo.read()
    print(linea)

#leo el archivo linea por linea
#dentro del parentesis indico la cantidad de caracteres que voy a leer
#linea = archivo.readline()


#devuelve una lista con todas las lineas del archivo
#lineas = archivo.readlines()

#cerrar el archivo
#archivo.close()#no es necesario cerrarlo usando with open

#muestro en pantalla.
#print(lineas)