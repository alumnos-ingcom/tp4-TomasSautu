################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número crack!") from err
    return entero

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=50):
    entero=(ingreso_entero(mensaje))
    if (entero >= valor_minimo and entero <= valor_maximo):
        
        return entero
    
    else:
        raise IngresoIncorrecto(f"{entero} no era un número entre 0 y 50 crack")
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            cantidad_reintentos = cantidad_reintentos-1
#             print(f"Te quedan {cantidad_reintentos} intentos")
    raise IngresoIncorrecto(f"Luego de 5 intentos")



class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 


def prueba():
    print("Inserta un número entre 0 y 50")
    numero = ingreso_entero("Largame el número ")
    numero = ingreso_entero_restringido("")
    numero = ingreso_entero_reintento()

if __name__ == "__main__":
    prueba()
    