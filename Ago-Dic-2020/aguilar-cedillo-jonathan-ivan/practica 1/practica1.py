class Matrix:
    def __init__(self, matrix_string):
        self.matrix_List = [[int(num) for num in e.split()] for e in matrix_string.splitlines()]

    def row(self, index):
        return list(self.matrix_List[index-1])

    def column(self, index):
        return [i[index-1] for i in self.matrix_List]

Matrix1 = Matrix("9 8 7 \n5 3 2 \n6 6 7")

print(Matrix1.matrix_List)
fila=int(input("fila a solicitar: " ))
columna=int(input("Columna a solicitra: "))
print(Matrix1.row(fila))
print(Matrix1.column(columna))
