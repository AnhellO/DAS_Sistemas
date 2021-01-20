class Matrix:
    def __init__(self, matrix_string):
         self.matrix_string = [[int(column) for column in row.split()] for row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix_string[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix_string]
    
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")

des = int(input("Seleccione 1 si quiere saber la fila o 2 para columna\n"))
if des == 1:
    row = matrix.row(int(input("Número de fila\n")))
    print(row)
if des == 2:
    column = matrix.column(int(input("Número de columna\n")))
    print(column)