CI = int(input("Ingrese el capital inicial:"))
TASA = float(input("Ingrese la taza de interes anual EXPRESADA EN DECIMAL:"))
T = int(input("Ingrese el tiempo expresado en AÑOS:"))
a = 12 * T
b = 1 + (TASA / 12)
ba = b ** a
InteresCompuesto = CI * ba

print("El interes compuesto es de:", InteresCompuesto) 