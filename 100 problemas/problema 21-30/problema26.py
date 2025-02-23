#IMPLEMENTAR UNA AGENDA DE CONTACTOS 
agenda = {}
def agregar(agenda, nombre, telefono):
    agenda[nombre] = telefono
def buscar(adenda, nombre):
    return agenda.get(nombre, "no existe")

sino = True
while sino == True:
    p = int(input("Introduzca el numero de lo que desea, (1)agregar un contacto, (2)buscar un contacto: "))
    if p == 1:
        nombre = input("Nombre: ")
        telefono = int(input("Telefono: "))
        agregar(agenda, nombre, telefono)
        print("Contacto añadido")
    elif p == 2:
        nombre = input("Nombre: ")
        print("Telefono:", buscar(agenda, nombre))
    else:
        print("Numero invalido")

    op = int(input("¿Desea seguir buscando o agregando contactos? (1)si, (2)no : "))
    if op == 1:
        sino = True
    elif op == 2:
        sino = False
    else:
        print("Valor invalido")

print("Fin")    
print("Agenda:", agenda)