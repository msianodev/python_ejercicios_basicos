import re

texto = '''"El 7 de diciembre de 1941, la Armada Imperial Japonesa
sorprendió a la flota de los Estados Unidos en Pearl Harbor, Hawái. El
ataque provocó la entrada de los Estados Unidos en la Segunda Guerra
Mundial como aliado de las Potencias Aliadas, y fue un factor fundamental
para la derrota de Japón en la guerra."'''

resultado1 = re.search(r"(\d{1,2}) de (\w+) de (\d{4})", texto)
#search busca la expresion regular que le pasamos como parametro en el texto
#esta funcion busca en el texto la expresion regular que le pasamos como parametro
#\d busca un digito numerico del 0 al 9
#{1,2} busca entre 1 y 2 digitos
#\w busca un caracter alfanumerico
#() agrupa la expresion regular
#el resultado de la busqueda se almacena en resultado
#para realizar el caso inverso debemos utilizar la letra en mayuscula

#->: \A busca el inicio de una cadena

#->: \b busca un limite de palabra

#->: \d busca un digito numerico del 0 al 9
#->: \D busca un caracter que no sea numerico

#->: \s busca un espacio en blanco
#->: \S busca un caracter que no sea un espacio en blanco
#->: . busca todos los caracteres excepto el salto de linea

#->: \w busca un caracter alfanumerico
#->: \W busca un caracter que no sea alfanumerico

#->: \Z busca el final de una cadena

resultado2 = re.findall(r"\d{1,2} de \w+ de \d{4}", texto)
#findall busca todas las coincidencias de la expresion regular que le pasamos como parametro en el texto

print(resultado1,resultado2)
