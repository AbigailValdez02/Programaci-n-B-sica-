#CALCULADORA DE ESTADISTICAS

import math 
def calculadora(*numeros):
    promedio = lambda nums: sum(nums) / len(nums)
    mediana= sorted(numeros)[len(numeros)//2]
    varianza = sum((x-promedio(numeros))**2 for x in numeros) / len(numeros)
    desviacion= math.sqrt(varianza)

    return promedio(numeros), mediana, desviacion

numeros = list(map(float, input("Ingrese numeros separados por espacio: ").split()))
print(calculadora(*numeros))