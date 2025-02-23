#verificar si un numero es primo
n = int(input("Ingrese un numero:"))

if n <= 1:
    print("El numero no es primo")
elif n == 2:
    print("El numero es primo")
elif n > 2:
    if n % 2 == 0:
        print("El numero no es primo")
    elif n == 3:
        print("El numero es primo")
    elif n % 3 == 0:
        print("El numero no es primo")
    else:
        print("El numero es primo")
