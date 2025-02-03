CI = int(input("Ingrese el capital inicial:"))
TASA = float(input("Ingrese la taza de interes anual EXPRESADA EN DECIMAL:"))
T = int(input("Ingrese el tiempo expresado en AÑOS:"))

InteresCompuesto = CI * [1 + (TASA / 12)] ** 12 * T