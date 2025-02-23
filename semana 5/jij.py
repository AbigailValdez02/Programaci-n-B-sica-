



menu1 = """
# Menu principal 
#
# E -> Exponentes 
# M -> Multiplicaciones 
# D -> Division
# A -> Adicion
# S -> Sustraccion
# X -> Salir
#
"""
bmenu1 = True

menu2 = """
# Menu division
#
# 1 -> Division
# 2 -> Division entera
# 3 -> Division residuo
# 4 -> Regresar a menu principal
#
"""
bmenu2 = None
bdiv0 = True

def exponentes(base, potencia):
    return base ** potencia

def multiplicacion(factor1, factor2):
    return factor1 * factor2

def divisor(dividendo, divisor):
    if divisor != 0:
        return dividendo / divisor 
    else:
        while bdiv0:
            nuevodivisor = int(input("La division entre cero es imposible, ingrese otro numero: "))
            if nuevodivisor != 0:
                bdiv0 = False
        return dividendo / nuevodivisor
    
def leernumeros():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    return num1, num2

def divisionmenu():
    while bmenu2:



while bmenu1:
    print(menu1)
    op = input("Ingrese la opion deseada: ")
    op = op.upper()
    if op == "E":