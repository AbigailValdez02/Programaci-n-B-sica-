#Convertir una temperatura entre distintas escalas

C = int(input("Ingrese la temperatura en grados Celsiuspara convertirla a otras escalas: "))

F = ((9/5) * C) + 32
K = C + 273.15
R = (C + 273.15) * (9/5)
Re = C * (4/5)

print("A Fahrenheit=", F)
print("A Kelvin=", K)
print("A Rankine=", R)
print("A Reaumur=", Re)