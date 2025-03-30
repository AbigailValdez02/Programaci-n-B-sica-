#IMPLEMENTACION DE MULTIPLES PARADIGMAS 
# Programación Orientada a Objetos (POO)
class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Programación Estructurada (Funciones bien definidas)
def calcular_factorial(n):
    """Calcula el factorial de un número usando un bucle (Imperativa)."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def ordenar_lista(lista):
    """Ordena la lista usando el algoritmo de burbuja (Imperativa)."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def buscar_elemento(lista, valor):
    """Busca un elemento en la lista (Imperativa)."""
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1

# --- Programa Principal ---
if _name_ == "_main_":
    # Uso de Programación Imperativa
    print("=== Programación Imperativa ===")
    num = int(input("Ingrese un número para calcular su factorial: "))
    print(f"Factorial de {num}: {calcular_factorial(num)}")

    # Uso de Programación Estructurada
    print("\n=== Programación Estructurada ===")
    lista = [34, 7, 23, 32, 5, 62]
    print(f"Lista original: {lista}")
    print(f"Lista ordenada: {ordenar_lista(lista)}")

    # Buscar un elemento en la lista
    valor = int(input("\nIngrese un número a buscar en la lista: "))
    posicion = buscar_elemento(lista, valor)
    if posicion != -1:
        print(f"El número {valor} está en la posición {posicion}.")
    else:
        print(f"El número {valor} no está en la lista.")

    # Uso de Programación Orientada a Objetos
    print("\n=== Programación Orientada a Objetos ===")
    persona = Persona("Carlos", 25)
    persona.mostrar_info()