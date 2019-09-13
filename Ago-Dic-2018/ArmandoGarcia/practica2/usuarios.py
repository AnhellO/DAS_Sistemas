# Ejercicio 9-3
class usuario:
    def __init__(self, first_name, last_name, semestre, escuela):
        self.first_name = first_name
        self.last_name = last_name
        self.semestre = semestre
        self.escuela = escuela

    def __str__(self):
        return 'Nombre: {} \nApellido: {} \nSemestre: {} \nEscuela: {}'.format(self.first_name,self.last_name,self.semestre,self.escuela)

usuario_1 = usuario('Luis','Rodas','Sexto','TEC Monterry')
usuario_2 = usuario('Alfonso','Hinojosa','Primero','Cbtis 300')
usuario_3 = usuario('Alexander','Jimenez','Decimo','Escuela de la vida')

print(usuario_1)
print('\n')
print(usuario_2)
print('\n')
print(usuario_3)
