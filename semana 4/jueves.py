

bandera = True
contador = 1
ListContactos = list()

while bandera:
    op = input(f"Cantidad de cintactos: {contador - 1} n Desea agregar un contacto?(S/N): ")
    if op.lower() == "s":
        contacto = dict()
        contacto["identificador"] = input(f"Ingrese el identificador de contacto {contador]")