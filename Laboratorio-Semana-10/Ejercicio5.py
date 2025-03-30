#EJERCICIO 5, MODULO PARA CONVERSOR DE UNIDADES

import conversor


while True:
    op= int(input("Ingrese la opcion a realizar \n 1) km a millas \n 2) celsius a fahrenheit \n 3) litros a galones \n 4) salir \n"))
    if op == 1:
        km = int(input("Ingrese los km a convertir \n km="))
        print(f"{km} km es igual a {km_a_millas(km)}")

    elif op == 2:
        c = int(input("Ingrese los grados celsius a convertir \n celsius:"))
        print(f"{c} grados celsius es igual a {celsius_a_fahrenheit(c)}")

    elif op == 3:
        litros = int(input("Ingrese los litros a convertir \n litros="))
        print(f"{litros} litros es igual a {litros_a_galones(litros)}")

    elif op == 4:
        print("Saliendo...")
        break

    else: 
        print("Opcion invalida")