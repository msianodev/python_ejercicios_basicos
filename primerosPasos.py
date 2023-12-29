#ejercicio práctico de conocimientos hasta el momento:
# 1. Hoy faltó el profesor de clases y los alumnos decidieron armar su propia clase, uno de sus alumnas va a ser su profesor y otro va ser de asistente:
# a. Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
# b. El mayor es el profesor y el menor es el asistente, quien es quien?


#funcion para obtener el asistente y al profesor segun la edad
# def obtener_compañeros(cantidad):
#     #creando una lista con los compañeros
# 	compañeros = []
# 	#ejecutando un for para pedir informacion a cada compañero
# 	for i in range (7):
# 		nombre = input("Ingrese el nombre del compañero: ")
# 		edad = int(input("Ingrese la edad del compañero: "))
# 		compañero = [nombre, edad]
# 		#agregando la informacion de cada compañero a la lista
# 		compañeros.append(compañero)
# 	#ordenando la lista de menor a mayor
# 	compañeros.sort(key=lambda x:x[1])
# 	#obteniendo el asistente siendo el primero de la lista
# 	asistente = compañeros[0][0]
# 	#obteniendo el profesor siendo el ultimo de la lista
# 	profesor = compañeros[-1][0]
# 	#retornando el asistente y el profesor
# 	return asistente, profesor
# #ejecutando la funcion obtener_compañeros y cargo 7 compañeros desempaquetando el resultado en asistente y profesor
# asistente, profesor = obtener_compañeros(7)
#imprimiendo el asistente y el profesor
# print("El asistente es: ", asistente)
# print("El profesor es: ", profesor)


# #Creando una funcion para obtener numeros primos
# def obtener_primos(cantidad):
# 	#recorro los numeros desde el 2 hasta el numero que me pasan
# 	for i in range(2, cantidad):
#      #si el resto de la division es 0, entonces no es primo
# 		if cantidad % i == 0: return False
# 	return True
    
# #creando una funcion para obtener los numeros primos hasta el numero que me pasan
# def numeros_primos_hasta(num):
# 	#creando una lista para guardar los numeros primos
# 	numeros_primos = []
# 	#recorro los numeros desde el 1 hasta el numero que me pasan mas 1
# 	for i in range (1, num+1):
# 		#ejecuto la funcion obtener_primos y si el resultado es True, agrego el numero a la lista
# 		resultado = obtener_primos(i)
# 		#si el resultado es True, agrego el numero a la lista
# 		if resultado == True: numeros_primos.append(i)
# 	#retorno la lista de numeros primos
# 	return numeros_primos

# #ejecutando la funcion numeros_primos_hasta y cargo el resultado en la variable resultado
# resultado = numeros_primos_hasta(100)
# #muestro la lista de resultados de primos
# print(resultado)


#Hacer una funcion que ejecute una serie de fibonacci con cualquier numero que le pasemos por parametro
# def fibonacci(cantidad):
# 	#creando una lista para guardar los numeros de la serie
# 	serie = []
# 	#creando una variable para guardar el numero anterior
# 	anterior = 0
# 	#creando una variable para guardar el numero actual
# 	actual = 1
# 	#recorro los numeros desde el 1 hasta el numero que me pasan
# 	for i in range (1, cantidad+1):
# 		#agrego el numero actual a la lista
# 		serie.append(actual)
# 		#guardo el numero actual en la variable anterior
# 		anterior = actual
# 		#guardo la suma del numero anterior y el actual en la variable actual
# 		actual = anterior + actual
# 	#retorno la lista de numeros de la serie
# 	return serie

# serie_fibonacci = fibonacci(5)
# print(serie_fibonacci)