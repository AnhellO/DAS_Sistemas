#!/usr/bin/env python

# Java war flashbacks intensifies...
class Matrix:
    def __init__(self, data):
        self.data = [[int(column) for column in row.split()] for row in data.splitlines()]

    def getRow(self, row_position):
        if not self.validateRow(row_position):
            return 'Woops... esa fila no existe...'
        else:
            return self.data[row_position-1]

    def getColumn(self, column_position):
        if not self.validateRow(column_position):
            return 'Woops... esa columna no existe...'
        else:
            return ([row[column_position-1] for row in self.data])

    def validateRow(self, row_position):
        # It will only work if it's a square matrix... LOL
        if row_position < 1 or row_position > len(self.data):
            return False
        else:
            return True

# Inputs
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
# Rows stufff
row_position = int(input('¿Qué fila desea mi estimado otaku?\n'))
rows = matrix.getRow(row_position)
print(rows)
# Columns stuff
column_position = int(input('¿Qué columna desea mi estimado otaku?\n'))
columns = matrix.getColumn(column_position)
print(columns)