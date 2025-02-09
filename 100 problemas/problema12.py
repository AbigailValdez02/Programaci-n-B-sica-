#Encontrar el mayor entre tres numeros dados


num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))

mayor = num1
if mayor > num2:
    mayor = mayor
else:
    mayor = num2
if mayor > num3:
    mayor = mayor
else:
    mayor = num3

print("El numero mayor es:", mayor)
