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
