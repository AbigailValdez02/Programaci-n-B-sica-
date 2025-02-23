#Calcular la suma de una serie numerica
numeros = []
c = int(input("Introduzca la cantidad de numeros de su serie: "))
cont = 0 

while cont < c : 
    n = int(input("Introduza un numero: "))
    numeros.append(n)
    cont = cont + 1

s = sum(numeros)
print(f"La suma de los numeros es: {s}")