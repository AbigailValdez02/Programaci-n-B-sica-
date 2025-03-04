#funcion que invierta cadena 
def Cinv(cadena):
    invertida = cadena[::-1]
    return invertida

cadena = input("Ingrese una palabra: ")
print(Cinv(cadena))



#FACTORIAL
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact 

#problema 6
def sumaNum(num):
    if num > 0:
         suma = 0 
         while num > 0:
              d =  num % 10
              suma = suma + d
              num = num // 10
    return suma


    
    
num = int(input("numero: "))
print(sumaNum(num))