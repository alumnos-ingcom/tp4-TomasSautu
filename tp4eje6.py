################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero
import random

def lista(cantidad_numeros):
    lista = []
    for i in range(cantidad_numeros):
        lista.append(random.randint(0, 200))
    return lista
    
def minimo(lista, contador):
    minimo = lista[0]
    
    for i in range(contador):
        
        if minimo < lista[i]:
            minimo = minimo

        else:
            minimo = lista[i]
            
    return minimo
    
def maximo(lista, contador):  
    maximo = lista[0]
    for i in range(contador):
        if maximo > lista[i]:
            maximo = maximo
        else:
            maximo = lista[i]
    return maximo


def prueba():
    cantidad = ingreso_entero("Cuántos números quiere en total?: ")
    listaNumeros = lista(cantidad)
    print(f"La lista de números creada es {listaNumeros}")
    numero = minimo(listaNumeros, cantidad)
    print(f"El número mínimo de la lista es {numero}")
    numero = maximo(listaNumeros, cantidad)
    print(f"El número máximo de la lista es {numero}")

if __name__ == "__main__":
    prueba()