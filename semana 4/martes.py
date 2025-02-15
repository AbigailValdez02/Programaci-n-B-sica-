 #busqueda lineal

from random import randint 



listaP = list()
listaN = list()
elementos = int(input("introduzca la cantidad de elementos: "))

for cont in range(-elementos, elementos):
    if cont < 0:
        listaN.append(randit(-100, 0))
    elif cont > 0:
        listaP.append(randint(1, 100))
    else:
        listaP.append(randint(0, 1))

listacompleta = listaN + listaP
print(listacompleta)
