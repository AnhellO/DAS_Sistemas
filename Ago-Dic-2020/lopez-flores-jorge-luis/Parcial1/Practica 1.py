class Matrix:
    def __init__(self, mtx_string):

        self.a = [[int(x) for x in i.split()] for i in mtx_string.splitlines()]

    #Declaramos la fila que se mostrará
    def row(self, indx):
        self.fila=self.a[:]
        return self.fila[indx-1]

    #Declaramos la columna que se mostrará
    def column(self, indx):
        return[self.a[i][indx-1] for i in range(len(self.a))]


#Mostramos la matriz
m = Matrix("9 8 7 \n 5 3 2 \n 6 6 7")
print(m.a)
print(m.row(int(input("Numero de fila:"))))
print(m.column(int(input("Numero de columna:"))))