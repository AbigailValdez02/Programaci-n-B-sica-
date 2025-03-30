#MANEJO DE INVENTARIO CON LISTAS Y DICCIONARIOS 
inventario={}
while True:

 opcion= int(input("seleccione la opcion a realizar:\n 1)Agregar prodducto \n 2)Eliminar producto \n 3)Buscar producto \n 4)Mostrar todos los productos \n Seleccion:"))
 if opcion==1:
    categoria=input("Ingrese la caterogoria del producto:")
    nombre=input("Ingrese el nombre del producto:")
    precio=input("Ingrese eel precio del producto:")
    cantidad=input("Ingrese cantidad del producto:")
    inventario[nombre]= {"Cateroria": categoria, "Precio": precio, "Cantidad": cantidad}

 elif opcion==2:
    eliminar= input("Ingrese el nombre del producto a eliminar:")
    if eliminar in inventario:
        inventario.pop(eliminar)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

 elif opcion ==3:
    buscar= input("Ingrese el nombre del producto a buscar:")
    if buscar in inventario:
        print(inventario.get(buscar))
    else:
        print("Producto no encontrado")

 elif opcion ==4:
    print(inventario)

 else:
    print("Opcion invalida")