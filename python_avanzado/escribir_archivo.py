with open("texto_prueba.txt",'w', encoding="UTF-8") as archivo: 
    # la w es de write, si no existe el archivo lo crea, si existe lo sobreescribe
    # si usamos a, es de append, si no existe el archivo lo crea, si existe agrega al final
    
    #sobreescribiendo el archivo completo
    archivo.write("Hola mundo")
    
    #de esta forma podemos escribir las lineas que queramos
    #archivo.writelines("Hola mundo!!!!!!!!!\n")