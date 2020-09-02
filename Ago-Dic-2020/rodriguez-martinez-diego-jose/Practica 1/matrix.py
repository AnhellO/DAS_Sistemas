class Matrix:

    def __init__(self, matrix_string = ""):
        # Creo una lista de listas a partir del matrix_string; e es cada elemento de matrix_string.splitlines 
        # (ej:'9 8 7'), e.split() es una lista hecha de cada iteracion de e (ej: [9,8,7])

        self.matrix_List = [[int(num) for num in e.split()] for e in matrix_string.splitlines()]

    def row(self, index):
        # Debido a la forma en la que construi la matriz, solo es cuestion de regresar el item de la lista
        # de listas que corresponde a index
        # retorno una lista de la row creada de los elementos del item que corresponde a la row del index
        # para no mantener relacion con matrix_list

        if len(self.matrix_List) != 0:
            return [i for i in self.matrix_List if i == self.matrix_List[index-1]][0]
        else:
            return []

    def column(self, index):
        # List comprehension que te regresa la columna que corresponde al indice; La idea es recorrer las rows
        # y acceder a la columna respectiva desde la lista del row

        return [i[index-1] for i in self.matrix_List]


###########
myMatrix = Matrix("1 2 3\n 4 5 6\n7 8 9")

print(myMatrix.row(1))
print(myMatrix.column(1))