class Matrix:
    matrix_List = []

    def __init__(self, matrix_string):
        #Creo una lista de listas a partir del matrix_string; e es cada elemento de matrix_string.split 
        # (ej:'9 8 7'), e.split() es una lista hecha de cada iteracion de e (ej: [9,8,7])
        #

        self.matrix_List = [[int(num) for num in e.split()] for e in matrix_string.split("\n")] 

    def row(self, index):
        #debido a la forma en la que construi la matriz, solo es cuestion de regresar el item de la lista
        #de listas que corresponde a index

        return self.matrix_List[index-1]

    def column(self, index):
        #List comprehension que te regresa la columna que corresponde al indice; La idea es recorrer las rows
        # mientras que la columna se queda fija en el valor del index  

        return [self.matrix_List[i][index-1] for i in range( len(self.matrix_List)) ]


###########
myMatrix = Matrix("9 8 7\n 5 3 2\n6 6 7")
print(myMatrix.row(1))
print(myMatrix.column(2))