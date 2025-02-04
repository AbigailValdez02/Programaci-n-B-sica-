num = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese el numero del cual desea saber si es multiplo:"))
if num % 2 == 0:
    print("El numero", num, "es par")
else:
    print("El numero es impar")

if num % num2 == 0:
    print("El numero", num ,"es multiplo de", num2)
else:
    print("El numero", num ,"no es multiplo de", num2)
