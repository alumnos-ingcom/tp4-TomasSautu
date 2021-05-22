################
# Tomás Sautú - @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero, IngresoIncorrecto


def convertir_a_centigrados(fahrenheit):
    
    centigrados = (fahrenheit - 32) * 5/9
    
    return centigrados

def convertir_a_fahrrenheit(centigrados):
    
    farenheit = (centigrados * 9/5) + 32
    
    return farenheit

def prueba():
        numero = ingreso_entero("Ingrese el número de los Grados Fahrenheit que quiere convertir en Centigrados: ")
        resultado = convertir_a_centigrados(numero)
        print(f"Los {numero}°F convertidos a centígrados son {resultado}°C")
        numero = ingreso_entero("Ingrese el número de los Grados Centigrados que quiere convertir a Fahrenheit: ")
        resultado = convertir_a_fahrrenheit(numero)
        print(f"Los {numero}°C convertidos a fahrenheit son {resultado}°F")

if __name__ == "__main__":
    prueba()