#SIMULAR EL LANZAMIENTO DE UN DADO Y UNA MONEDA 
import random
def dado():
    return random.randint(1,6)

def moneda():
    r = random.choice(["Cara", "Cruz"])
    return r 

s = int(input("Seleccione una opcion: (1)Lanzamiento de dado, (2)Lanzamiento de moneda: "))
if s == 1 :
    print(f"El resultado fue: {dado()}")
elif s == 2:
    print(f"El resultaddo fue: {moneda()}")
else:
    print("Numero invalido")
    