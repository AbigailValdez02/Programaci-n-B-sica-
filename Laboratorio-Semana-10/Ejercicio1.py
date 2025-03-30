#Ejercicio 1: ANALISIS DE TEXTOS CON DICCIONARIOS Y CONJUNTOS

# Solicitar el texto al usuario
texto = input("Ingrese un texto para analizar: ").lower()

# Reemplazar signos de puntuación con espacios y dividir en palabras
for caracter in ",.;:!?":
    texto = texto.replace(caracter, "")

palabras = texto.split()

# Usar un conjunto para contar palabras únicas
palabras_unicas = set(palabras)

# Usar un diccionario para contar la frecuencia de cada palabra
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Encontrar la palabra más frecuente
palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
frecuencia_maxima = frecuencia_palabras[palabra_mas_frecuente]

# Mostrar resultados
print("\n=== Análisis del Texto ===")
print(f"Número total de palabras: {len(palabras)}")
print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")
print("\nFrecuencia de cada palabra:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia} veces")
print(f"\nLa palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_maxima} apariciones.")