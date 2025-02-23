#Generar la secuencia de fibbonacci hasta un numero dado de terminos
n = int(input("Ingrese el numero de terminos:"))
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_secuencia = [0, 1]
    for n in range (2, n):
     fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])
    return fib_secuencia
print(fibonacci(n))