#Implementar distintos metodos de ordenamiento

#1) Por Seleccion:
lista = [5, 7, 3, 1, 9 ,2, 8, 4, 6]
longitud = len(lista)
for i in range(longitud - 1):
    menor = i
    for j in range (i + 1, longitud):
        if lista[j] < lista[menor]: 
            menor = j 
    temporal = lista[menor]
    lista[menor] = lista [i]
    lista[i] = temporal
print(lista)


#2) Ordenamiento burbuja 
lista2 = [3, 6, 2, 7, 1, 4, 5]
for i in range(len(lista2) - 1):
    for j in range(len(lista2) - 1):
        if lista2[j] > lista2[j + 1]:
            lista2[j], lista2[j + 1] = lista2[j + 1],  lista2[j]
print(lista2)

#3) Por incersion:
lista3 = [16, 19, 14, 18, 17, 15]
for i in range(1,len(lista3)):
    actual = lista3[i]
    indice = i

    while indice > 0 and lista3[indice - 1] > actual :
        lista3[indice] = lista3[indice - 1] 
        indice = indice - 1
    lista3[indice] = actual
print(lista3)
