class Matrix:
    def __init__(self, m_string):
        self.matriz = [[x for x in i.split()] for i in m_string.splitlines()]
        
    def row(self, index):
        self.row=self.matriz[index-1]
        return self.row

    def column(self, index):
        return [self.matriz[c][index-1]
        for c in range(len(self.matriz[:]))]

        

m=Matrix("9 8 7\n5 3 2\n6 6 7")
print(m.matriz)
print(m.row(int(input('ingresa el numero de fila: '))))
print(m.column(int(input('ingresa el numero de columna: '))))

