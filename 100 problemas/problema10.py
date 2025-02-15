#Leer, escribir y modificar un archivo de texto

archivo = ejemplo.txt

#escribir en el archivo
with open(archivo, "w") as f:
    f.write("Este es un archivo de ejmplo. \nTercera linea del archivo. ")


#Leer el archivo
with open(archivo, "r") as f:
    contenido = f.read()
    print("Contenido original:")
    print(contenido)

#Modificar el archivo 
with open(archivo, "a") as f:
    f.write("\nNueva linea añadida. ")