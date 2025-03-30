#EJERCICIO 7, ORDENAMIENTO Y BUSQUEDA

import random

# Pedir al usuario el tamaño de la lista
n = int(input("Ingrese el tamaño de la lista: "))

# Generar lista de números aleatorios
lista = [random.randint(1, 100) for _ in range(n)]

print("\nLista original:")
print(lista)

# Implementación de Quicksort directamente
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)

# Ordenar la lista con Quicksort
lista = quicksort(lista)

print("\nLista ordenada:")
print(lista)

# Pedir al usuario un número para buscar en la lista
num_buscar = int(input("\nIngrese el número a buscar: "))

# Implementación de búsqueda binaria directamente
izquierda, derecha = 0, len(lista) - 1
encontrado = False

while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == num_buscar:
        encontrado = True
        break
    elif lista[medio] < num_buscar:
        izquierda = medio + 1
    else:
        derecha = medio - 1

# Mostrar el resultado de la búsqueda
if encontrado:
    print(f"El número {num_buscar} fue encontrado en la posición {medio}.")
else:
    print(f"El número {num_buscar} no está en la lista.")