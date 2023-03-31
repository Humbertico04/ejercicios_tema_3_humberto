# Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de 
# forma recursiva y de forma iterativa

class Matriz:
    def __init__(self, filas, columnas, matriz=None):
        self.filas = filas
        self.columnas = columnas
        if matriz is None:
            self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
        else:
            self.matriz = matriz

    def obtener_elemento(self, fila, columna):
        return self.matriz[fila][columna]

    def asignar_elemento(self, fila, columna, valor):
        self.matriz[fila][columna] = valor

    def __str__(self):
        return str(self.matriz)

def sarrus_iterativo(matriz):
    if matriz.filas != matriz.columnas or matriz.filas != 3:
        raise ValueError("La matriz debe ser cuadrada de 3x3")

    resultado = 0
    for i in range(matriz.columnas):
        diagonal_principal = 1
        diagonal_secundaria = 1
        for j in range(matriz.filas):
            diagonal_principal *= matriz.obtener_elemento(j, (i + j) % matriz.columnas)
            diagonal_secundaria *= matriz.obtener_elemento(j, (i - j) % matriz.columnas)
        resultado += diagonal_principal - diagonal_secundaria

    return resultado

matriz = Matriz(3, 3, [[1, 0, 0], [0, 10, 0], [0, 0, 1]])

print("Matriz:")
print(matriz)

print("Determinante iterativo:", sarrus_iterativo(matriz))