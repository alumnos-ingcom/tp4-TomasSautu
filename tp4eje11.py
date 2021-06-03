################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero

def palindromo(texto):
    texto = texto.replace(" ","")
    texto = texto.lower
    largo = len(texto)
    
    if largo % 2 == 0:
        izquierda = texto[:largo // 2]
        derecha = texto[largo // 2:]
    else:
        izquierda = texto[:largo// 2]
        derecha = texto[largo // 2 + 1:]
        
    return izquierda == derecha[::-1]


def prueba():
    texto = input("Ingrese una palabra o texto para saber si es palindromo o no: ")
    resultado = palindromo(texto)
    if resultado == True:
        print(f'"{texto}" es un palindromo')
    else:
        print(f'"{texto}" no es palindromo')


if __name__ == "__main__":
    prueba()