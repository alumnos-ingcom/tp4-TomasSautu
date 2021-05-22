################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def signo(numero):
    
    if (numero == 0):
        return "El número es cero"
    if (numero > 0):
        return "El número es positivo (+)"
    else:
        return "El número es negativo (-)"

def prueba():
    numero = ingreso_entero("Ingrese un número para decirle si es positivo o negativo: ")
    valor = signo(numero)
    print(valor)
    

if __name__ == "__main__":
    prueba()