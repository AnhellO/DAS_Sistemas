class Matrix:
    def __init__(self, matrix_string):#constructor de la clase
        self.matrix_string = [[int(num) for num in lista.split()] for lista in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix_string[index-1]
        
    def column(self, index):
        return [self.matrix_string[i][index-1] for i in range(len(self.matrix_string))]
        
matriz = Matrix("9 8 7\n 5 3 2\n6 6 7") #Creo la instancia de la clases
print(matriz.row(1))
print(matriz.column(2))