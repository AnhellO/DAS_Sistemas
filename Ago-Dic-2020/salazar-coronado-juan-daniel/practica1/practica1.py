class Matrix:
    def __init__(self, matrix_string):
        #aquí se crea una variable donde la matriz se separa por los saltos de linea y después las listas
        #que están dentro se separán por los espacios, para así poder sacar las columnas, ya que si solo
        #se deja separado por los saltos de linea al momento de querer imprimir las columnas no sale nada
        #ya que en las listas separadas por saltos de linea se toma como si solo hubiera un valor el cual
        #estaría ubicado en el indice 0
        self.matrizfilas = [[int(x) for x in i.split()] for i in matrix_string.splitlines()]

    def row(self, index):
        #se retorna la lista separada por saltos de linea que se indica de una copia de la matriz donde
        #se creo originalmente para que no tenga cambios o problemas la matriz original
        return self.matrizfilas[index-1].copy()
        

    def column(self, index):
        #se retorna directamente la columna que se indica, tomando el indice que se le pide de cada una
        #de las listas separadas por saltos de linea
        return [i[index-1] for i in self.matrizfilas]
        

print ("Matriz de prueba: ")
matrizdeejemplo = Matrix("9 8 7\n5 3 2\n6 6 7")

print (matrizdeejemplo.matrizfilas)
print ("En esta matriz de prueba solo hay 3 filas y 3 columnas")
print (matrizdeejemplo.row(int(input("Número de fila requerido: "))))
print (matrizdeejemplo.column(int(input("Número de columna requerido: "))))
