################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def es_primo(numero):
    for i in range(2,numero):
        if numero % i == 0 :
            return False
        else:
            return True


def prueba():
    numero = ingreso_entero("Ingrese un número para saber si es primo: ")
    primo = es_primo(numero)
    if primo == True:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")

if __name__ == "__main__":
    prueba()