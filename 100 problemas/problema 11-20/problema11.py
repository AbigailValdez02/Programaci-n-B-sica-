#Verificar si una cadena es un palindromo

def esPalindromo(palabra):
    palabra = palabra.lower()#cambia mayusculas a minusculas
    palabra = palabra.replace(" ", "") #reemplaza lo que esta en la izquierda por lo que esta en la derecha (quito los espacios)
    palabra = palabra.replace("á", "a") #reemplaza las vocales con tilde 
    palabra = palabra.replace("é", "e") 
    palabra = palabra.replace("í", "i") 
    palabra = palabra.replace("ó", "o") 
    palabra = palabra.replace("ú", "u") 

    a = 0
    b = len(palabra) - 1

    for i in range (0, len(palabra)):
        if palabra [a] == palabra [b]:
            a += 1
            b -= 1
        else:
            return False
    return True



palabra = str(input("Ingrese una palabra o frase: "))
if esPalindromo(palabra):
    print("Es una palabra o frase palindroma")
else:
    print("No es palindroma")