#Implementar busqueda binaria y lineal

#busqueda lineal 
print("Busqueda lineal")
def busquedaLineal (lista, elem):
    i = 0
    for z in lista :
        if (z == elem):
            return 1
        i = i + 1
    return -1

def main():
    lista = (1, 8, 14, 19, 23, 27, 33, 39, 45, 50, 59, 67, 73, 79)
    elem = 23
    pos = busquedaLineal(lista, elem)
    if (pos>-1):
        print("La posicion es : ", pos + 1)
    else :
        print("El elemento no se encuentra en la lista")
main()


