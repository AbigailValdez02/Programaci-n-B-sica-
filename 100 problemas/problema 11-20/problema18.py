#Resolver ecuaciones cuadraticas 

import math

print("Ingrese los valores de 'a', 'b' y 'c' de su ecuacion cuadratica")
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

D = b **2 - 4*a*c
if D > 0 :
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("Las soluciones de la ecuacion son:")
    print("x1=", r1, "x2=", r2)
elif D == 0:
    r = (-b + math.sqrt(D)) / (2*a) 
    print("La solucion de la ecuacion es unica")
    print("x=", r)
else:
    print("La ecuacion no tiene solucion real")

