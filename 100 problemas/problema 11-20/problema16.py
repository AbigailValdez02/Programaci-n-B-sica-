#Contar el numero de vocales y consonantes en una cadena

vocales = ("a", "e", "i", "o", "u")
consonantes = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

v = 0
c = 0 
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()
for letra in cadena:
    if letra in vocales:
        v += 1
    elif letra in consonantes:
        c += 1
    
print(f"La cadena tiene {v} vocales y {c} consonantes")
