################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número genio!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos= 5):
    intentos = cantidad_reintentos
    while intentos >= 0:
        try: 
            return ingreso_entero(mensaje)        
        except:
            print(f"Te quedan {intentos} champion")
            intentos = intentos - 1
    raise IngresoIncorrecto("No era un número titan!")


def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=50):
    entero = ingreso_entero(mensaje)
    if (entero >= valor_minimo and entero <= valor_maximo):
        return entero
    else:
        raise IngresoIncorrecto(f"{entero} no era un número entre 0 y 50 fiera")




class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 


def prueba():
    numero = ingreso_entero("Largame el número crack: ")
    print(f"Tu número es {numero}, titan")
    numero = ingreso_entero_reintento("Largame un número capitan: ")
    print(f"Tu número es {numero}, ídolo")
    numero = ingreso_entero_restringido("Inserta un número entre el 0 y el 50: ")
    print(f"Este fué tu número {numero}, master")

if __name__ == "__main__":
    prueba()
    