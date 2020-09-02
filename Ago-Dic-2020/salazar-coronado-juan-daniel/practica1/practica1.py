class Matrix:
    def __init__(self, matrix_string):
        #aquí se crea una variable donde se guarde la matriz normal
        self.matrizcompleta = matrix_string.split()
        #aquí se crea una variable donde la matriz se separa por los saltos de linea y después las listas
        #que están dentro se separán por los espacios, para así poder sacar las columnas, ya que si solo
        #se deja separado por los saltos de linea al momento de querer imprimir las columnas no sale nada
        #ya que en las listas separadas por saltos de linea se toma como si solo hubiera un valor el cual
        #estaría ubicado en el indice 0
        self.matrizfilas = [[x for x in i.split()] for i in matrix_string.splitlines()]

    def row(self, index):
        #se crea una variable para que guarde la lista separada por saltos de linea que se le indica
        self.fila = self.matrizfilas[index-1]
        return self.fila

    def column(self, index):
        #se crea una variable donde guarda los valores en la posición que se le indique dentro de las listas
        #que están separadas por saltos de linea, así va tomando solo el indice que se le indica dentro de
        #cada lista separada por espacios, intenté usar el comando self.columna = [i for i in self.matrizfilas[i][index-1]]
        #para que hiciera lo mismo pero me lo tomaba como si i no había sido definida, y cambiandolo por
        #esté comando ya funciona
        self.columna = [i[index-1] for i in self.matrizfilas]
        return self.columna

print ("Matriz de prueba: ")
matrizdeejemplo = Matrix("9 8 7\n5 3 2\n6 6 7")

print (matrizdeejemplo.matrizcompleta)
print ("En esta matriz de prueba solo hay 3 filas y 3 columnas")
print (matrizdeejemplo.row(int(input("Número de fila requerido: "))))
print (matrizdeejemplo.column(int(input("Número de columna requerido: "))))
