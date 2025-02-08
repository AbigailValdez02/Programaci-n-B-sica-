

#operadores relacionales y logicos en if
#igualdad (=), diferente (!=), mayor que (>), menor que (<)


#tipo de dato bool: dos valores: verdadero y falso 
#0 y non son false 



#CICLOS: FOR Y WHILE 

#ciclo while: se ejecuta mientras una condicion seaa verdadera
#ciclo for: tiene una cantidad de ciclos determinados  

#COMPONENTES ESENCIALES DE LOS CICLOS:
#inicializacion, condicion, 


#objetos iterables: list [], tuple () (0,0), set (conjunto), dict {} 
#ejemplo 
saludos = dict()
saludos["Español"] = "Hola Mundo"
saludos["Ingles"] = "Hello World"
saludos["Feancais"] = "Bonjour Mondieu"

for idioma, saludos in saludos.items():
    print(idioma, saludos)






estudiambre = dict()
estudiambre["nombre"] = "Abigail"
estudiambre["carrera"] = "LA"
estudiambre["matricula"] = "2148352"





primos = [1,2,3,5,7,11,13,17,19,23,29,31]
listprimos = list()
for num in range(0,32):
    if num in primos:
        print(num)
print(listprimos)
print