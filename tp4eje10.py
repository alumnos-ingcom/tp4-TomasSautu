################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def factores_primos(numero):
    factores = []
    
    if numero > 0 :
        for i in range(2,numero+1):
            while numero % i == 0:
                factores.append(i)
                numero = numero / i
        return factores
    else:
        return False

def prueba():
    numero = ingreso_entero("Inserte un número pasitivo para que el programa escriba sus factores primos: ")
    resultado = factores_primos(numero)
    if resultado != False:
        print(f"Los factores primos de {numero} son {resultado}")
    else:
        print(f"El número {numero} es negativo")
    
    

if __name__ == "__main__":
    prueba()