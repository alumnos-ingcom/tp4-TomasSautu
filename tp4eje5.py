################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def signo(numero):
    
    if (numero == 0):
        return 0
    if (numero > 0):
        return 1
    else:
        return -1

def prueba():
    numero = ingreso_entero("Ingrese un número para decirle si es positivo o negativo: ")
    valor = signo(numero)
    if valor == 0:
        print(f"El número es {numero}")
    else:
        if valor > 0 :
            print(f"El número {numero} es positivo (+)")
        else:
            print(f"El número {numero} es negativo (-)")
    

if __name__ == "__main__":
    prueba()