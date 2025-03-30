

#SISTEMA DE GESTION DE VEHICULOS 

# Definición de la clase base Vehiculo
class Vehiculo:
    def _init_(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}")

# Subclase Automovil
class Automovil(Vehiculo):
    def _init_(self, marca, modelo, anio, precio, num_puertas):
        super()._init_(marca, modelo, anio, precio)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.num_puertas}")

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def _init_(self, marca, modelo, anio, precio, cilindrada):
        super()._init_(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}cc")

# Programa principal
print("\n--- Registro de Vehículos ---")
tipo = input("Ingrese el tipo de vehículo (automovil/motocicleta): ").strip().lower()

marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo: ")
anio = int(input("Ingrese el año: "))
precio = float(input("Ingrese el precio: "))

if tipo == "automovil":
    num_puertas = int(input("Ingrese el número de puertas: "))
    vehiculo = Automovil(marca, modelo, anio, precio, num_puertas)
elif tipo == "motocicleta":
    cilindrada = int(input("Ingrese la cilindrada: "))
    vehiculo = Motocicleta(marca, modelo, anio, precio, cilindrada)
else:
    print("Tipo de vehículo no válido.")
    vehiculo = None

if vehiculo:
    print("\nInformación del vehículo registrado:")
    vehiculo.mostrar_info()