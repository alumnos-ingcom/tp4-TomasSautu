################
# Tomás Sautú - @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4eje1 as suma

def suma_lenta(numeroUno, numeroDos):
    
    resultadoSuma = numeroUno + numeroDos
    
    if numeroUno < resultadoSuma:
        while numeroUno < resultadoSuma:
            numeroUno = numeroUno+1
    else:
        while numeroUno > resultadoSuma:
            numeroUno = numeroUno-1
    return numeroUno
        

def prueba():
    print("Inserta dos número para ser sumados de forma lenta")
    numero_1 = suma.ingreso_entero("Inserta el primer número: ")
    numero_2 = suma.ingreso_entero("Inserta el segundo número: ")
    resultado = suma_lenta(numero_1, numero_2)
    print(resultado)

if __name__ == "__main__":
    prueba()