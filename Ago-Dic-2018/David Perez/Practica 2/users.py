# Ejercicio 9-3 ----------------------------------------------------------------
class user:
    def __init__(self, first_name, last_name, semester, collage):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester
        self.collage = collage
    def __str__(self):
        return 'Nombre: {} \nApellido: {} \nSemestre: {} \nCarrera: {}'.format(self.first_name,self.last_name,self.semester,self.collage)

user_1 = user('David','Pérez','Septimo','ISC')
user_2 = user('Andrés','López','Sexto','ITIC')
user_3 = user('Armando','Paredes','Septimo','Industrial')

print('\n {}'.format(usuario_1))
print('\n {}'.format(usuario_2))
print('\n {}'.format(usuario_3))
