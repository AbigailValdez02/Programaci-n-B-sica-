#Busqueda binaria  (los numeros de la lista tienen que estar ordenados)
print("Busqueda binaria")
def busquedaBinaria(list, ele):
    pi = 0
    pf = len(list)-1
    while (pi < pf):
        pm = int((pi + pf) / 2)
        if  (list[pm] == ele ) :
            return pm 
        elif (list[pm] < ele) :
            pi = pm + 1
        else :
            pf = pm - 1
    return -1

def main():
    list = (7, 16, 21, 29, 33, 39, 47, 52, 61, 68, 69, 70, 76, 85, 90, 99)
    ele = 29
    p = busquedaBinaria(list, ele)
    if (p > -1):
        print("La posicion es : ", p + 1)
    else :
         print("El elemento no se encuentra en la lista")
main()