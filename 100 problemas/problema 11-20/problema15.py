#Determinar si un año es bisiesto

año = int(input("Ingrese año: "))

b = (año % 4 == 0 and año % 100 == 0)
if (año % 4 == 0 and año % 100!= 0 ):
    print("Si es bisiesto")
elif (b and año % 400 == 0):
    print("Si es bisiesto")
else:
    print("No es bisiesto")