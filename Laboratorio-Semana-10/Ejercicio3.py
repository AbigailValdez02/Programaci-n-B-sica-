#GESTION DE CONTACTOS CON TUPLAS Y ESTRUCTURAS ANIDADAS

Agenda= []

while True:
    op= int(input("Seleccione la opcion a realizar:\n 1)Agregar contacto \n 2)Buscar contacto \n 3)Lista de contactos  \n 4)Salir \n seleccion:"))
    if op == 1:
        nombre = input("Ingrese nombre de conacto:").lower()
        numero = input("Ingrese numero:")
        correo = input("Ingrese correo del contacto:")
        Agenda.append((nombre, numero, correo))

    elif op == 2:
        contacto = input("Introduzca el nombre del contacto a buscar:")
        for contacto in Agenda:
            if contacto[0].lower() == nombre.lower():
                print(f"Nombre: {contacto[0]}, Numero: {contacto[1]}, Correo: {contacto[2]}")
            else:
                print("Contacto no encontrado")

    elif op == 3:
        for contacto in sorted(Agenda):
            print(f"Nombre: {contacto[0]}, Numero: {contacto[1]}, Correo : {contacto[2]}")
    
    elif op== 4:
        print("Byee")
        break 