#Ejercicio 9-5 -----------------------------------------------------------------
class user:
    def __init__(self, first_name, last_name, semester, collage):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester
        self.collage = collage
        self.access = 0

    def __str__(self):
        return 'Nombre: {} \nApellido: {} \nSemestre: {} \nCarrera: {} \nIntentos de acceso: {}'.format(self.first_name,self.last_name,self.semester,self.collage,self.access)

    def login_attempts(self):
        self.access += 1

    def reset_login_attempts(self):
        self.access = 0

user_1 = user('David','Pérez','Septimo','ISC')
user_2 = user('Andrés','López','Sexto','ITIC')
user_3 = user('Armando','Paredes','Septimo','Industrial')

print('\n {}'.format(user_1))
print('\n {}'.format(user_2))
print('\n {}'.format(user_3))
user_3.login_attempts()
print('\n {}'.format(user_3))
user_3.reset_login_attempts()
print('\n {}'.format(user_3))
