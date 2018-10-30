class usuario:
    def __init__(self, first_name, last_name, semestre, escuela,intentos_de_acceso = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.semestre = semestre
        self.escuela = escuela
        self.intentos_de_acceso = intentos_de_acceso

    def __str__(self):
        return 'Nombre: {} \nApellido: {} \nSemestre: {} \nEscuela: {} \nIntentos de acceso: {}'.format(self.first_name,self.last_name,self.semestre,self.escuela,self.intentos_de_acceso)

    def login_attempts(self,n):
        self.intentos_de_acceso +=n

    def reset_login_attempts(self):
        self.intentos_de_acceso = 0

usuario_1 = usuario('Luis','Rodas','Sexto','TEC Monterry')
usuario_2 = usuario('Alfonso','Hinojosa','Primero','Cbtis 300')
usuario_3 = usuario('Alexander','Jimenez','Decimo','Escuela de la vida')

print(usuario_1)
print('\n')
print(usuario_2)
print('\n')
print(usuario_3)
print('\n')
usuario_3.login_attempts(1)
print(usuario_3)
print('\n')
usuario_3.reset_login_attempts()
print(usuario_3)
