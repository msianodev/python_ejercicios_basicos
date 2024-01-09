#creando mipropia excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Mensaje de primera excepcion: {err}")
        
#Lanzando la excepcion
#raise MiExcepcion("Mi primera excepcion")

#Manejo de excepcion
try:
    raise MiExcepcion("Mi primera excepcion")
except:
    print("Se lanzo la excepcion")