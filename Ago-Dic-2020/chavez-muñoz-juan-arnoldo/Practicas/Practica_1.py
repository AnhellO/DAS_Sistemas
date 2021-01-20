class Matrix:
    matrix_string = [[9, 8, 7], 
    [5, 3, 2],
    [6, 6, 7]]
    

    def __init__(self, matrix_string):
        pass

    def row(self, index):
            return print(f'La fila {index} es: '+str( self.matrix_string[index-1]))
        

    def column(self, index):
        columnas = []
        for i in range(len(self.matrix_string)):
            for j in range(len(self.matrix_string[i])):
                if (j == index-1):
                    columnas.append(self.matrix_string[i][j])  
        return print(f'La columna {index} es: '+str(columnas))

matriz = Matrix(matrix_string=()) #Creo la instancia de la clase
matriz.row(3)
matriz.column(3)


