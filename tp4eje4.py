################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def comparacion(numeroUno, numeroDos):
    if numeroUno < numeroDos:
        return -1
    if numeroUno > numeroDos:
        return 1
    else:
        return 0
    
def prueba():
    numero_1 = ingreso_entero("Ingrese el primer número: ")
    numero_2 = ingreso_entero("Ingrese el segundo número: ")
    resultado = comparacion(numero_1, numero_2)
    print(resultado)

if __name__ == "__main__":
    prueba()