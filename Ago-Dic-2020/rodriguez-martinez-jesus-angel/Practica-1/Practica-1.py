#!/usr/bin/env python

# Java war flashbacks intensifies...
class Matrix:
    def __init__(self, data):
        self.data = [[int(column) for column in row.split()] for row in data.splitlines()]

    def get_row(self, row_position):
        return list(self.data[row_position-1])

    def get_column(self, column_position):
        return list([row[column_position-1] for row in self.data])

# Inputs
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
# Rows stufff
row_position = int(input('¿Qué fila desea mi estimado otaku?\n'))
rows = matrix.get_row(row_position)
print(rows)
# Columns stuff
column_position = int(input('¿Qué columna desea mi estimado otaku?\n'))
columns = matrix.get_column(column_position)
print(columns)