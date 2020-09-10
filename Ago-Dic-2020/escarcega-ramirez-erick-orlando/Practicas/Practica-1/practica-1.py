class Matrix:
    def __init__(self, matrix_string):
       self.matrix = [[int(a) for a in line.split()] for line in matrix_string.splitlines()]

    def row(self, row):
        return (self.matrix.copy())[row-1]

    def column(self, col):
        #return [self.matrix[k][col-1] for k in enumerate(len(self.matrix))]
        return [k[col-1] for k in (self.matrix.copy())]
        
end = Matrix("9 8 7\n5 3 2\n6 6 7")

print(end.row(1))
print(end.column(2))