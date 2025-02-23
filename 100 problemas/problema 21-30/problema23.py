#IMPLEMENTAR Y OPERAR CON MATRICES  

A = [[1, 2, 7, 5],
     [8, 3, 0, 2],
     [3, 2, 9, 6]]

B = [[7, 2, 8, 0],
     [1, 0, 3, 8],
     [2, 6, 3, 4]]

def sumar_matrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    else:
        return None
    
c = sumar_matrices(A, B)
if c == None:
    print("No se pueden sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end= " ")
        print("]")
