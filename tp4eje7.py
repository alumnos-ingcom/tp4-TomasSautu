################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def division_lenta(dividendo, divisor):
    resto = 0
    cociente = 0
    
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        resto = dividendo
        cociente = cociente + 1
    
    return (cociente, resto)

def prueba():
    print("""Este programa le pedira el ingreso de dos nuúmeros para dividir uno con otro y
hara que mediante restas sucesivas, obtenga el valor del cociente y resto de la división
""")
    dividendo = ingreso_entero("Ingrese el número que quiere dividir: ")
    divisor = ingreso_entero("Ingrese el número por el cual lo quiere dividir: ")
    cociente, resto = division_lenta(dividendo, divisor)
    print(f"El cociente es {cociente} y el resto es {resto}")

if __name__ == "__main__":
    prueba()