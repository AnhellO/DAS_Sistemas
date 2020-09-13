import split
class Matriz(str):
    def __init__(self, string):
        #Separaramos nuestro string por los saltos de linea y cada salto de linea lo separamos por espacios vacios para asi obtener una lista
        self.string = [[x for x in h.split(" ")] for h in string.splitlines()]

    def row(self, index):  
        #Regresa la parte de la lista que se refiera a ese numero de fila 
        num = self.string[index-1]
        return print(f"Los valores en la fila {index} son: {num}")

    def column(self,index):
        #Regresas la columna gracias al indice
        num = [x[index-1] for x in self.string]
        return print(f"Los valores en la columna {index} son: {num}")


if __name__ == "__main__":
    x= Matriz("9 8 7\n5 3 2\n6 6 7")
    print(x.string)
    print(x.row(1))
    print(x.column(1))

