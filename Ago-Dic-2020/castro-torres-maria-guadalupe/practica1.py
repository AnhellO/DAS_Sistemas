class Matriz:
    def __init__(self, m_string):
       
        self.a = [[int(x) for x in i.split()] for i in m_string.splitlines()]

    def filas(self, ind):
        self.fila=self.a[:]
        return self.fila[ind-1]


    def columna(self, ind):
        return[self.a[i][ind-1] for i in range(len(self.a))]
    


m = Matriz("9 8 7 \n 5 3 2 \n 6 6 7")
print (m.a)
print (m.filas(int(input("ingresa el numero de fila que necesites:"))))
print (m.columna(int(input("ingresa el numero de columna que necesites:"))))        

