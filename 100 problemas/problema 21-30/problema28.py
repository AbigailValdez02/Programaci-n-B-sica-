#SIMULAR UNA CUENTA BANCARIA CON DEPOSITOS Y RETIROS 

saldo = 1000
print("*****MENU*****")
print("1. Depositar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible de la cuenta")
print("4. Salir")
op = int(input("Ingrese la opcion deseada"))
print()
if op == 1:
    s = float(input("Ingrese la cantidad a depositar: "))
    saldo += s
    print(f"Su nuevo saldo es: {saldo}")

elif op == 2:
    r = float(input("Ingrese la cantidad a retirar: "))
    if r > saldo:
        print("No tiene esa cantidad a retirar")
    else:
        saldo -= r
        print(f"Su nuevo saldo es: {saldo}")

elif op == 3:
    print(f"El dinero en la cuenta es:{saldo}")

elif op == 4:
    print("¡Nos vemos!")

else:
    print("Error, ese valor es invalido")