

def contador(cadena):
    cadena = cadena.lower()
    vocales = {"a": [], "e": [], "i": [], "o": [], "u": []}
    for indice, caracter in enumerate(cadena):
        if caracter in vocales :
            vocales[caracter].append(indice)
    return vocales

cadena=input("c" )
print(contador(cadena))
