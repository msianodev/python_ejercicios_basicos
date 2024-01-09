#armar 2 listas, una con nombres y otra con apellidos, cantidad = 10
nombres = ["Juan","Pedro","Maria","Jose","Luis","Ana","Carlos","Jorge","Miguel","Pablo"]
apellidos = ["Gonzalez","Garcia","Rodriguez","Fernandez","Lopez","Martinez","Sanchez","Perez","Gomez","Martin"]

#registrar esta informacion en un archivo txt de forma optima
# with open("archivo_datos.txt","w") as archivo:
#     for i in range(10):
#         archivo.write(nombres[i]+","+apellidos[i]+"\n")

#hecho a la forma del curso de dalto
with open("nombres_y_apellidos.txt","w")as arch:
    arch.writelines("los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n") for n,a in zip(nombres,apellidos)]
    
