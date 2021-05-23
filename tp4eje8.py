################
# Tomás Sautú- @TomasSautu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4eje1 import ingreso_entero


def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos:
        mayor = uno
        menor = dos
    else:
        mayor = dos
        menor = uno
    if mayor > tres:
        mayor = mayor
        intermedio = tres
    else:
        intermedio = mayor
        mayor = tres
    if menor > intermedio:
        Intermedio = menor
        menor = intermedio
    else:
        Intermedio = intermedio
        menor = menor
        
    return(menor, Intermedio, mayor)
        
    
def ordenar_menor_a_mayor(uno, dos, tres):
    if uno > dos:
        mayor = uno
        menor = dos
        
    else:
        mayor = dos
        menor = uno
        
    if mayor > tres:
        mayor = mayor
        intermedio = tres
        
    else:
        intermedio = mayor
        mayor = tres
        
    if menor > intermedio:
        Intermedio = menor
        menor = intermedio
        
    else:
        Intermedio = intermedio
        menor = menor
        
    return(menor, Intermedio, mayor)





def prueba():
    print("""Este programa hará que a partir de tres variables de tipo entero retorne una tupla con dichos valores
Primero ordenados de menor a mayor
y Segundo ordenas de mayor a menor""")
    numero_1 = ingreso_entero("Ingrese el primer número: ")
    numero_2 = ingreso_entero("Ingrese el segundo número: ")
    numero_3 = ingreso_entero("Ingrese el tercer número: ")
    uno, dos, tres = ordenar_mayor_a_menor(numero_1, numero_2, numero_3)
    print(f"El orden de mayor a menor es {tres, dos, uno}")
    uno, dos, tres = ordenar_menor_a_mayor(numero_1, numero_2, numero_3)
    print(f"El orden de menor a mayor es {uno, dos, tres}")
    

if __name__ == "__main__":
    prueba()