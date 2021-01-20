#Pratica 1: Solicitar numero de filas y columnas
class Matriz:
    def __init__(self, matrix_str):
        self.lista = [[int(i) for i in j.split()] for j in matrix_str.splitlines()]

    def row(self, fila):
        return list(self.lista[fila-1])

    def column(self, column):
        return [i[column-1] for i in self.lista]

matriz = Matriz("5 4 3 \n 6 1 9 \n 1 8 7")
print(matriz.lista)
fila=input("Número de Fila a Solicitar: " )
columna=input("Número de Columna a Solicitar: ")
print("No. de Fila: ", matriz.row(int(fila)))
print("No. de Columna: ", matriz.column(int(columna)))