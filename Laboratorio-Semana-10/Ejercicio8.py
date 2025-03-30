#IMPLEMENTACION DE MERGESORT

# Pedir al usuario los números a ordenar
lista = list(map(int, input("Ingrese números separados por espacio: ").split()))

print("\nLista original:")
print(lista)

# Implementación de Mergesort sin módulos
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenar cada mitad recursivamente
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Combinar las dos mitades ordenadas
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Ordenar la lista
lista = merge_sort(lista)

print("\nLista ordenada:")
print(lista)