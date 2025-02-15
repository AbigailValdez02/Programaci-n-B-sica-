#IMPLEMENTAR ESTRUCTURAS DE DATOS BASICAS:PILA, COLA Y LISTA ENLAZADA 

#pilas (ultimo en entrar es el primero en salir)
pila = [1,2,3,4,5,6,7,8,9]
print(pila)
#Agregando elementos por el final de la fila
pila.append(10) 
pila.append(11)
print(pila)
#Sacando elementos por el final
n = pila.pop()
print(f"El elemento sacado fue: {n}")
n = pila.pop()
print(f"El elemento sacado fue: {n}")
print(pila)


#Colas (primero en entrar es el primero en salir)
cola = ["Abigail", "Juan", "Armando", "Carlos", "Regina", "Lety"]
print(cola)
#Agregamos elementos al final de la cola 
cola.append("Karla")
cola.append("Roberto")
cola.append("Raul")
print(cola)
#sacando elementos por el principio de la cola
c= cola.pop(0) #indice de primer elemento
print(f"atendiendo a {c}")
print(cola)
c= cola.pop(0) #indice de primer elemento
print(f"atendiendo a {c}")
print(cola)


#lista enlazada 
