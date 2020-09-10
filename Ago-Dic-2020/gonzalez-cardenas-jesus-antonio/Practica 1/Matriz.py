class Matrix:
    def __init__(self, matrix_string):
        
        self._matrix_string = [[int(row_item) for row_item in row.split()] for row in matrix_string.split("\n")]   

    def row(self, index):
        
        return self._matrix_string[index - 1]

    def column(self, index):
        
        return [column_item[index - 1] for column_item in self._matrix_string]
        
mtrx = Matrix("1 2 3\n4 5 6\n7 8 9")
print(mtrx.row(1))
print(mtrx.column(1))