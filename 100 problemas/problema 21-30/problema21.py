#CALCULAR EL AREA Y VOLUMEN DE DISTINTAS FIGURASS GEOMETRICAS 

def a_cuadrado(lado):
    area = lado **2
    print(f"Area = {area}")

def a_rectangulo(base, altura):
    area = base * altura 
    print(f"Area = {area}")

def a_circulo(radio):
    area = (3.1416) *  ((radio) **2)
    print(f"Area = {area}")

def v_cubo(lado):
    vol= lado ** 3
    print(f"Volumen = {vol}")

def v_esfera(radio):
   vol = (4/3) * (3.1416) * ((radio) ** 3)
   print(f"Volumen = {vol}")
   
def v_cilindro(radio, altura):
    vol = (3.1416) * ((radio) ** 2) * (altura)
    print(f"Volumen = {vol}")



print("Seleccione la opcion que requiera:")
print("(1) Area de un cuadrdo")
print("(2) Area de un rectangulo")
print("(3) Area de un circulo")
print("(4) Volumen de un cubo")
print("(5) Volumen de una esfera")
print("(6) Volumen de un cilindro")
seleccion = int(input("Introduzca numero del 1 al 6: "))

if seleccion == 1 :
    lado = int(input("Ingrese cuanto mide un lado del cuadrado: "))
    print(a_cuadrado(lado))
elif seleccion == 2:
    base = int(input("Ingrese cuanto mide la base del rectangulo: "))
    altura = int(input("Ingrese cuanto mide la altura del rectangulo: "))
    print(a_rectangulo(base, altura))
elif seleccion == 3:
    radio = int(input("Ingrese cuanto mide el radio del circulo: "))
    print(a_circulo(radio))
elif seleccion == 4:
    lado = int(input("Ingrese cuanto mide un lado del cubo: "))
    print(v_cubo(lado))
elif seleccion == 5:
     radio = int(input("Ingrese cuanto mide el radio de la esfera: "))
     print(v_esfera(radio))
elif seleccion == 6:
     radio = int(input("Ingrese cuanto mide el radio del cilindro: "))
     altura = int(input("Ingrese cuanto mide la altura del cilindro: "))
     print(v_cilindro(radio, altura))
else: 
    print("Valores invalidos")
