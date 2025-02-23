#CREAR UN CONVERSOR DE UNIDADES

op_medidas = int(input("***MENU PRINCIPAL***\n1. MEDIDAS DE LONGITUD\n2. MEDIDAS DE VOLUMEN\n3. MEDIDAS DE PESO\nEscoja la opcion deseada"))
if op_medidas == 1:
    print("***MEDIDAS DE LONGITUD***")
    op_long = int(input("Escoja una opcion\n1. Pulgadas a milimetros\n2. Yardas a metros"))
    if op_long == 1:
        p = int(input("Ingrese las pulgadas a convertir: "))
        r = p * 25.40
        print(f"{p} pulgadas es igual a {r} milimetros")
    elif op_long == 2:
        y = int(input("Ingrese las yardas a convertir: "))
        r = y * 0.9144
        print(f"{y} yardas es igual a {r} metros")
    else:
        print("Valor invalido")

elif op_medidas == 2:
     print("***MEDIDAS DE VOLUMEN***")
     op_vol = int(input("Escoja una opcion\n1. Pie cubicos a metros cubicos\n2. Yardas cubicas a metros cubicos"))
     if op_vol == 1:
        p = int(input("Ingrese los pies cubicos a convertir: "))
        r = p * 0.02832
        print(f"{p} pies cubicos es igual a {r} metros cubicos")
     elif op_vol == 2:
        y = int(input("Ingrese las yardas cubicas a convertir: "))
        r = y * 0.7646
        print(f"{y} yardas cubicas es igual a {r} metros cubicos")
     else:
        print("Valor invalido")

elif op_medidas == 3:
    print("***MEDIDAS DE PEESO***")
    op_peso = int(input("Escoja una opcion\n1. Onzas a gramos\n2. Libras a kg"))
    if op_peso == 1:
        o = int(input("Ingrese las onzas a convertir: "))
        r = o * 28.35
        print(f"{p} onzas es igual a {r} gramos")
    elif op_peso == 2:
        l = int(input("Ingrese las libras a convertir: "))
        r = l * 0.45359
        print(f"{l} libras es igual a {r} kg")
    else:
        print("Valor invalido")

else:
    print("Valor invalido")