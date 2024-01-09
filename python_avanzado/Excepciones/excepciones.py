#defino una funcion para sumar dos numeros base 10
def sumar_dos_numeros_base_10():
    #ejecuto un while para que siempre se cumpla la condicion
    while True:
        #mientras que no se ingresen numeros, se ejecuta el while
        #ingreso 2 numeros
        a = input("Ingrese Numero 1: ")
        b = input("Ingrese Numero 2: ")
        #ejecuto un try para que si se ingresa un valor que no sea un numero, se ejecute el except
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            #Utilizo Exception porque es la clase padre de las excepciones, la capturo en e y luego muestro el mensaje de error
            print("Ingrese solo numeros")
            print(f"Error: {e}")
        else:
            #si se ingresan numeros, se ejecuta el break para que salga del while
            #else se ejecuta si no se ejecuta el except
            break
        finally:
            #siempre se ejecuta el finally
            print("Se ejecuto el finally")
    return resultado
print(sumar_dos_numeros_base_10())