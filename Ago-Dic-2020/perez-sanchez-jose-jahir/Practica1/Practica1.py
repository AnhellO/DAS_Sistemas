class Matriz(str):
    def __init__(self, string):
        #Separaramos nuestro string por los saltos de linea y cada salto de linea lo separamos por espacios vacios para asi obtener una lista
        self.matriz = [[x for x in h.split()] for h in string.splitlines()]

    def row(self, index):  
        #Regresa la parte de la lista que se refiera a ese numero de fila 
        return f"Los valores en la fila {index} son: {self.matriz[index-1].copy()}"

    def column(self,index):
        #Regresas la columna gracias al indice
        return f"Los valores en la columna {index} son: {[x[index-1] for x in self.matriz]}"


if __name__ == "__main__":
    x = Matriz("9 8 7\n5 3 2\n6 6 7")
    print(x.matriz)
    print(x.row(1))
    print(x.column(1))

