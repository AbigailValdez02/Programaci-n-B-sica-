#PROBLEMA 9
limite = int(input("Ingrese un nuero: "))

par = {}
Impar = {}
for num in range (1,limite+1):
    if num % 2 == 0:
        par.append(num)
    else:
        Impar.append(num)

Temario = max(len(par),len(Impar))

for item in range(Temario):
    try:
        print
