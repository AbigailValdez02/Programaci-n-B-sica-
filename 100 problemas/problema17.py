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
class node:
    def __init__(self, value):
        self.value = value
        self.Next = None

    def __str__(self):
        return str(self.value)
    
class listaEnlazada:
    def __init__(self):
        self.first = None
        self.size = 0

    def Append(self,value):
        MyNode = Node(value)
        if self.size == 0:
            self.first = MyNode 
        else:
            current = self.first 
            while current.Next != None:
                current = current.Next
            current.Next = MyNode 
        
        self.size += 1
        return MyNode 
    
    def Remove(self,value):
        if self.size == 0:
            return False
        else:
            current = self.first
            while current.Next.value != value:
                if current.Next == None:
                    return False
                else:
                    current = current.Next
            DeletedNode = current.Next
            current.Next = DeletedNode.Next

        self.size -= 1

        return DeletedNode

    def __len__(self):
        return self.size
    
    def __str__(self):
        string = "["
        current  = self.first
        while current != None:
            string += str(current)
            string += str(",")
            current = current.Next
        string += "]"

        return string



Mylist = listaEnlazada()

Mylist.Append(1)
Mylist.Append(2)
Mylist.Append(3)
Mylist.Append(4)

print(Mylist)
