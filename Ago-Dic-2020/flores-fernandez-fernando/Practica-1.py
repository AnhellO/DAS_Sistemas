import numpy as np
class Matrix:
    def __init__(self):
        pass
  
    def row(self):
        matriz = [
                 [9, 8, 7],
                 [5, 3, 2],
                 [6, 6, 7]
                 ]
        mnp = np.array(matriz)

        i = int(input("Numero de Fila que quisiera ver\n")) 
        i=i-1
        fila = mnp[i,:]
        print(fila)

   
    def column(self):
        matriz = [
                 [9, 8, 7],
                 [5, 3, 2],
                 [6, 6, 7]
                 ]
        mnp = np.array(matriz)

        
        i = int(input("Numero de Columna que quisiera ver\n")) 
        i=i-1
        columna = mnp[:,i]
        print(columna)
        
        
Matriz= Matrix()
des = int(input("Seleccione 1 si quiere saber la fila o 2 para columna\n"))
if des == 1:
    Matriz.row()
if des ==2:
    Matriz.column()