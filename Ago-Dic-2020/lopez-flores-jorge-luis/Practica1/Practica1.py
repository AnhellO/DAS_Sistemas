
class Matrix:
    def __init__(self, matrix_string):
        self.lista = [[int(i) for i in j.split()] for j in matrix_string.splitlines()]

    def row(self, fila):
        return list(self.lista[fila-1])

    def column(self, column):
        return [i[column-1] for i in self.lista]

matriz = Matrix("9 8 7 \n5 3 2 \n6 6 7")
print(matriz.lista)
fila=input("fila a solicitar: " )
columna=input("Columna a solicitra: ")
print("Fila ", matriz.row(int(fila)))
print("Columna ", matriz.column(int(columna)))